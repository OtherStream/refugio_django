# productos/urls.py

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api-crud', views.ProductoViewSet, basename='producto-api')
router.register(r'api-categorias', views.CategoriaViewSet, basename='categoria-api')

urlpatterns = [
    # Lista pública de productos
    path('', views.lista_productos, name='productos'),
    
    path('crear/', views.gestionar_producto_view, name='producto_crear'),
    path('editar/<int:pk>/', views.gestionar_producto_view, name='producto_editar'),
    
    path('toggle-disponible/', views.toggle_disponible_view, name='producto_toggle_disponible'),
    
    # URLs de la API
    path('', include(router.urls)),
]