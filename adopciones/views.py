from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.db import transaction
import json
import os 

from .models import Solicitud  
from animales.models import Animal 

def lista_adoptados_view(request):
    return render(request, 'adopciones/adoptados.html')

@login_required 
def lista_solicitudes_view(request):
    if request.method == 'POST' and request.user.is_staff:
        try:
            data = json.loads(request.body)
            solicitud_id = int(data.get('id_solicitud'))
            nuevo_estado = data.get('aceptado')

            with transaction.atomic():
                solicitud = Solicitud.objects.get(id=solicitud_id)
                solicitud.aceptado = nuevo_estado
                solicitud.save()

                animal = solicitud.animal
                if nuevo_estado == 'A':
                    animal.estatus = 'adoptado'
                    Solicitud.objects.filter(animal=animal, aceptado='P').update(aceptado='R')
                elif nuevo_estado == 'R':
                    if animal.estatus != 'adoptado':
                        animal.estatus = 'activo' 
                animal.save()

            return JsonResponse({'success': True, 'message': 'Estado actualizado correctamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

    solicitudes = None
    if request.user.is_staff:
        solicitudes = Solicitud.objects.all().select_related('usuario', 'animal').order_by('-fecha_solicitud')
    else:
        solicitudes = Solicitud.objects.filter(usuario=request.user).select_related('animal').order_by('-fecha_solicitud')

    context = { 'solicitudes': solicitudes }
    return render(request, 'adopciones/lista_solicitudes.html', context)


# --- 2. FUNCIÓN DE SEGURIDAD PARA VALIDAR ARCHIVOS ---
def validar_extension(archivo):
    ext_validas = ['.pdf', '.jpg', '.jpeg', '.png']
    # Obtiene la extensión del archivo (ej: .pdf) y la pone en minúsculas
    ext = os.path.splitext(archivo.name)[1].lower()
    return ext in ext_validas


# --- VISTA DE PROCESAR SOLICITUD ---
def procesar_solicitud_view(request):
    
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False, 
            'message': 'Tienes que estar logeado para solicitar adoptar'
        }, status=401)

    if request.method == 'POST':
        try:
            animal_id = int(request.POST.get('animal_id'))
            comprobante_file = request.FILES.get('comprobante_domicilio')
            ine_file = request.FILES.get('ine')

            if not comprobante_file or not ine_file:
                return JsonResponse({'success': False, 'message': 'Debes subir ambos archivos.'}, status=400)

            # --- 3. APLICAMOS LA VALIDACIÓN DE SEGURIDAD ---
            if not validar_extension(comprobante_file):
                return JsonResponse({'success': False, 'message': 'El Comprobante debe ser PDF, JPG o PNG.'}, status=400)
            
            if not validar_extension(ine_file):
                return JsonResponse({'success': False, 'message': 'La INE debe ser PDF, JPG o PNG.'}, status=400)

            animal = get_object_or_404(Animal, id=animal_id)
            usuario = request.user

            if animal.estatus != 'activo':
                return JsonResponse({'success': False, 'message': 'Este animal ya no está disponible.'})

            with transaction.atomic():
                Solicitud.objects.create(
                    usuario=usuario,
                    animal=animal, 
                    aceptado='P',
                    comprobante_domicilio=comprobante_file,
                    ine=ine_file
                )
                # No cambiamos estatus a inactivo, permitimos más solicitudes
                
            return JsonResponse({'success': True, 'message': '¡Solicitud registrada con éxito!'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=400)
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)