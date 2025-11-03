# adopciones/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Esta es la línea que causaba el error, ahora corregida:
    path('adoptados/', views.lista_adoptados_view, name='lista_adoptados'),
    
    # Las otras URLs que ya creamos:
    path('solicitudes/', views.lista_solicitudes_view, name='lista_solicitudes'),
    path('solicitud/crear/', views.procesar_solicitud_view, name='procesar_solicitud'),
]