from django.shortcuts import render
from avisos.models import Publicacion  

def index(request):
    avisos = Publicacion.objects.all()
    
    context = {
        'avisos': avisos
    }
    
    return render(request, "core/index.html", context)