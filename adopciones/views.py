from django.shortcuts import render
from animales.models import Animal


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