# adopciones/urls.py

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api-solicitudes', views.SolicitudViewSet, basename='solicitud-api')

urlpatterns = [
    path('adoptados/', views.lista_adoptados_view, name='lista_adoptados'),
    path('solicitudes/', views.lista_solicitudes_view, name='lista_solicitudes'),
    path('solicitud/crear/', views.procesar_solicitud_view, name='procesar_solicitud'),
    path('', include(router.urls)),
]