# productos/urls.py

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# 1. Creamos un router para la API
router = DefaultRouter()
# 'api-crud' será el prefijo para la API
router.register(r'api-crud', views.ProductoViewSet, basename='producto-api')

urlpatterns = [
    # 2. Esta es tu URL de la página web (la que ya tenías)
    # URL: /productos/
    path('', views.lista_productos, name='productos'),

    # 3. Estas son las URLs de tu nueva API (se agregan al router)
    # URL: /productos/api-crud/  (para listar y crear)
    # URL: /productos/api-crud/<pk>/ (para ver, actualizar, borrar)
    path('', include(router.urls)),
]