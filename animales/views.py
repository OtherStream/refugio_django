from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Animal
from .forms import AnimalForm # Importamos el formulario que creamos
from django.core.paginator import Paginator

def lista_animales_adoptar(request):
    # Obtenemos todos los animales (activos e inactivos)
    # y los ordenamos por estatus (para que los activos salgan primero)
    animales_list = Animal.objects.filter(estatus__in=['activo', 'inactivo']).order_by('estatus')
    
    # Configuramos el Paginator
    paginator = Paginator(animales_list, 8) # 8 animales por página
    
    # Obtenemos el número de página de la URL (ej. ?page=1)
    page_number = request.GET.get('page')
    
    # Obtenemos los objetos de esa página
    page_obj = paginator.get_page(page_number)
    
    # Pasamos el 'page_obj' a la plantilla
    context = {
        'page_obj': page_obj
    }
    return render(request, 'animales/adoptar.html', context)

# --- Vista nueva para Crear y Editar Animales ---

# Función para verificar si el usuario es staff (admin)
def es_admin(user):
    return user.is_staff

@login_required          # 1. Requiere iniciar sesión
@user_passes_test(es_admin, login_url='login') # 2. Requiere ser admin (si no, redirige al login)
def gestionar_animal_view(request, pk=None):
    animal = None
    if pk:
        # Si 'pk' (Primary Key) existe, estamos EDITANDO
        animal = get_object_or_404(Animal, pk=pk)
    
    # Esta lógica maneja tanto el GET (mostrar) como el POST (guardar)
    if request.method == 'POST':
        # Pasamos request.FILES para manejar la subida de la imagen
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('adoptar') # Redirige a la lista de animales
    else:
        # Si es GET, solo muestra el formulario (vacío o con datos)
        form = AnimalForm(instance=animal)
        
    return render(request, 'animales/gestionar_animal.html', {
        'form': form,
        'animal': animal # Lo pasamos para cambiar el título (Agregar/Editar)
    })