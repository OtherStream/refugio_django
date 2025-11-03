# adopciones/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.db import transaction
import json

# --- IMPORTACIONES CORREGIDAS ---
# Importamos Solicitud desde ESTA app (.models)
from .models import Solicitud  
# Importamos Animal desde la app 'animales'
from animales.models import Animal 
# --------------------------------

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import SolicitudSerializer

def lista_adoptados_view(request):
    """
    Esta vista simplemente muestra la página estática de 
    adopciones exitosas (el carrusel).
    """
    return render(request, 'adopciones/adoptados.html')

@login_required 
def lista_solicitudes_view(request):
    
    # --- LÓGICA DE API (POST) ---
    if request.method == 'POST' and request.user.is_staff:
        try:
            data = json.loads(request.body)
            solicitud_id = int(data.get('id_solicitud'))
            nuevo_estado = data.get('aceptado') # 'A' o 'R'

            with transaction.atomic():
                solicitud = Solicitud.objects.get(id=solicitud_id)
                solicitud.aceptado = nuevo_estado
                solicitud.save()

                animal = solicitud.animal
                if nuevo_estado == 'A':
                    animal.estatus = 'adoptado'
                elif nuevo_estado == 'R':
                    animal.estatus = 'activo' 
                animal.save()

            return JsonResponse({'success': True, 'message': 'Estado actualizado correctamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

    # --- LÓGICA DE VISTA (GET) ---
    solicitudes = None
    if request.user.is_staff:
        solicitudes = Solicitud.objects.all().select_related('usuario', 'animal').order_by('-fecha_solicitud')
    else:
        solicitudes = Solicitud.objects.filter(usuario=request.user).select_related('animal').order_by('-fecha_solicitud')

    context = {
        'solicitudes': solicitudes
    }
    return render(request, 'adopciones/lista_solicitudes.html', context)


@login_required 
def procesar_solicitud_view(request):
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            animal_id = int(data.get('animal_id'))

            # Ahora 'Animal' SÍ se refiere al de 'animales.models'
            animal = get_object_or_404(Animal, id=animal_id)
            usuario = request.user

            if animal.estatus != 'activo':
                return JsonResponse({'success': False, 'message': 'Este animal ya no está disponible.'})

            with transaction.atomic():
                # 'Solicitud' espera un 'Animal' de 'animales.models'
                Solicitud.objects.create(
                    usuario=usuario,
                    animal=animal, # <-- Ahora esto funcionará
                    aceptado='P' 
                )
                
                animal.estatus = 'inactivo'
                animal.save()

            return JsonResponse({'success': True, 'message': '¡Solicitud registrada con éxito!'})

        except Exception as e:
            # Mandamos el error real al frontend para depurar
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=400)
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

class SolicitudViewSet(viewsets.ModelViewSet):
    """
    API REST para el modelo Solicitud (un modelo relacionado).
    - GET: Lista todas las solicitudes.
    - POST: Crea una nueva solicitud.
    - PUT/PATCH: Actualiza una solicitud.
    - DELETE: Borra una solicitud.
    """
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer