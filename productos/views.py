from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Producto, Categoria
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import ProductoSerializer, CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required, user_passes_test
# Quitamos la importación de ProductoForm, ya no la usamos aquí
import json

def lista_productos(request):
    return render(request, 'productos/productos.html')

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria']

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

def es_admin(user):
    return user.is_staff

@login_required
@user_passes_test(es_admin, login_url='login')
def gestionar_producto_view(request, pk=None):
    """
    Esta vista ahora solo carga el HTML.
    JavaScript se encargará de hacer GET, POST, PATCH y DELETE a la API.
    """
    producto = None
    if pk:
        producto = get_object_or_404(Producto, pk=pk)
        
    return render(request, 'productos/gestionar_producto.html', {
        # Solo pasamos el 'producto' para que JS sepa si es 'editar' y tenga el ID
        'producto': producto 
    })