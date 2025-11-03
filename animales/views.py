from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Animal
from .forms import AnimalForm # Importamos el formulario que creamos
from django.core.paginator import Paginator

def lista_animales_adoptar(request):
    # Obtenemos todos los animales (activos e inactivos)
    # y los ordenamos por estatus (para que los activos salgan primero)
    animales_list = Animal.objects.filter(estatus__in=['activo', 'inactivo']).order_by('estatus')
    
    paginator = Paginator(animales_list, 8) 
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    
    # Pasamos el 'page_obj' a la plantilla
    context = {
        'page_obj': page_obj
    }
    return render(request, 'animales/adoptar.html', context)

# Vista nueva para Crear y Editar Animales 

# Función para verificar si el usuario es staff (admin)
def es_admin(user):
    return user.is_staff

@login_required          
@user_passes_test(es_admin, login_url='login') 
def gestionar_animal_view(request, pk=None):
    animal = None
    if pk:
        animal = get_object_or_404(Animal, pk=pk)
    
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('adoptar') 
    else:
        
        form = AnimalForm(instance=animal)
        
    return render(request, 'animales/gestionar_animal.html', {
        'form': form,
        'animal': animal 
    })