# animales/views.py

from django.shortcuts import render
from .models import Animal
from django.core.paginator import Paginator # 1. Importamos Paginator

def lista_animales_adoptar(request):
    # Obtenemos todos los animales (activos e inactivos)
    # y los ordenamos por estatus (para que los activos salgan primero)
    animales_list = Animal.objects.filter(estatus__in=['activo', 'inactivo']).order_by('estatus')
    
    # 2. Configuramos el Paginator
    paginator = Paginator(animales_list, 8) # 8 animales por página (tu 'limite')
    
    # 3. Obtenemos el número de página de la URL (ej. ?page=1)
    page_number = request.GET.get('page')
    
    # 4. Obtenemos los objetos de esa página
    page_obj = paginator.get_page(page_number)
    
    # 5. Pasamos el 'page_obj' a la plantilla
    context = {
        'page_obj': page_obj
    }
    return render(request, 'animales/adoptar.html', context)