# productos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import ProductoSerializer, CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend

# --- NUEVAS IMPORTACIONES ---
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ProductoForm 
# --------------------------


def lista_productos(request):
    # ... (Tu vista de lista de productos se queda igual) ...
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'productos/productos.html', {'productos': productos})

class ProductoViewSet(viewsets.ModelViewSet):
    # ... (Tu ViewSet de Producto se queda igual) ...
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria']

class CategoriaViewSet(viewsets.ModelViewSet):
    # ... (Tu ViewSet de Categoría se queda igual) ...
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# --- AGREGA ESTA NUEVA VISTA COMPLETA ---

def es_admin(user):
    return user.is_staff

@login_required
@user_passes_test(es_admin, login_url='login')
def gestionar_producto_view(request, pk=None):
    producto = None
    if pk:
        # Si hay 'pk', es para EDITAR
        producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        # Si se envía el formulario (POST)
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos') # Redirige a la lista pública de productos
    else:
        # Si se visita la página (GET)
        form = ProductoForm(instance=producto)
        
    return render(request, 'productos/gestionar_producto.html', {
        'form': form,
        'producto': producto
    })