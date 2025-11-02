from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import transaction
from .models import Solicitud, Animal # Importa Solicitud y Animal
import json


def lista_adoptados(request):
    animales = Animal.objects.filter(estado='Adoptado')
    return render(request, 'adopciones/adoptados.html', {'animales': animales})

def adoptar(request, animal_id):
    animal = get_object_or_404(AnimalAdopcion, id=animal_id)
    animal.estado = 'Adoptado'
    animal.save()
    return render(request, 'adopciones/detalle_adopcion.html', {'animal': animal})

def lista_adoptados_view(request):
    """
    Esta vista simplemente muestra la página estática de 
    adopciones exitosas.
    """
    # Solo le decimos que renderice el archivo HTML
    return render(request, 'adopciones/adoptados.html')

@login_required # Protegemos la vista, solo usuarios logueados pueden entrar
def lista_solicitudes_view(request):
    
    # --- LÓGICA DE API (POST) ---
    if request.method == 'POST' and request.user.is_staff:
        try:
            # Obtenemos los datos del POST
            data = json.loads(request.body)
            solicitud_id = int(data.get('id_solicitud'))
            nuevo_estado = data.get('aceptado') # 'A' o 'R'

            # Usamos una transacción para asegurar que ambas BBDD se actualicen
            with transaction.atomic():
                # 1. Actualizamos la solicitud
                solicitud = Solicitud.objects.get(id=solicitud_id)
                solicitud.aceptado = nuevo_estado
                solicitud.save()

                # 2. Actualizamos el estado del animal
                animal = solicitud.animal
                if nuevo_estado == 'A':
                    animal.estatus = 'adoptado'
                elif nuevo_estado == 'R':
                    animal.estatus = 'activo' # Vuelve a estar disponible
                animal.save()

            return JsonResponse({'success': True, 'message': 'Estado actualizado correctamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

    # --- LÓGICA DE VISTA (GET) ---
    solicitudes = None
    if request.user.is_staff:
        # El admin ve todas las solicitudes
        # .select_related() optimiza la consulta para traer usuario y animal
        solicitudes = Solicitud.objects.all().select_related('usuario', 'animal').order_by('-fecha_solicitud')
    else:
        # El usuario normal solo ve las suyas
        solicitudes = Solicitud.objects.filter(usuario=request.user).select_related('animal').order_by('-fecha_solicitud')

    context = {
        'solicitudes': solicitudes
    }
    return render(request, 'adopciones/lista_solicitudes.html', context)