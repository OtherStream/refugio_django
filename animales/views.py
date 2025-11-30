from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Animal
from .forms import AnimalForm 
from django.core.paginator import Paginator

def lista_animales_adoptar(request):
    animales_list = Animal.objects.filter(estatus='activo').order_by('nombre')
    
    paginator = Paginator(animales_list, 8) 
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }
    return render(request, 'animales/adoptar.html', context)

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