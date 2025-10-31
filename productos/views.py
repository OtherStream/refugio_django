# productos/views.py

from django.shortcuts import render
from .models import Producto

# --- Tu vista actual (Déjala como está) ---
def lista_productos(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'productos/productos.html', {'productos': productos})

# --- AGREGA ESTO (para la API) ---
from rest_framework import viewsets
from .serializers import ProductoSerializer # Importa el serializer que creaste

class ProductoViewSet(viewsets.ModelViewSet):
    """
    Este ViewSet maneja todo el CRUD (Crear, Leer, Actualizar, Borrar)
    para el modelo Producto.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer