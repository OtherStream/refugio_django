from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'productos/productos.html', {'productos': productos})


from rest_framework import viewsets
from .serializers import ProductoSerializer 

class ProductoViewSet(viewsets.ModelViewSet):
    """
    Este ViewSet maneja todo el CRUD (Crear, Leer, Actualizar, Borrar)
    para el modelo Producto.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer