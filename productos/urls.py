from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'api-crud', views.ProductoViewSet, basename='producto-api')

urlpatterns = [

    path('', views.lista_productos, name='productos'),

    path('', include(router.urls)),
]