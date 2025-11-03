
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import ProductoSerializer, CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ProductoForm 


def lista_productos(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'productos/productos.html', {'productos': productos})

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
    producto = None
    if pk:
        producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        # Si se envía el formulario (POST)
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos') 
    else:
        # Si se visita la página (GET)
        form = ProductoForm(instance=producto)
        
    return render(request, 'productos/gestionar_producto.html', {
        'form': form,
        'producto': producto
    })
    
@login_required
@user_passes_test(es_admin, login_url='login') # Solo los admins 
def toggle_disponible_view(request):

    if request.method == 'POST':
        try:
            # Obtenemos el ID del producto desde el JSON enviado
            data = json.loads(request.body)
            producto_id = int(data.get('id'))
            
            producto = get_object_or_404(Producto, id=producto_id)
            
            producto.disponible = not producto.disponible 
            producto.save()
            
            # Devuelve el nuevo estado
            return JsonResponse({'success': True, 'disponible': producto.disponible})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)