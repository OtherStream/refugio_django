from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'productos/productos.html', {'productos': productos})