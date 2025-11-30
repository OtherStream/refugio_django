# avisos/urls.py

from django.urls import path
from .views import (
    PublicacionListView, 
    PublicacionCreateView, 
    PublicacionUpdateView, 
    PublicacionDeleteView
)

urlpatterns = [
    # Muestra la lista de publicaciones (URL: /publicaciones/)
    path('', PublicacionListView.as_view(), name='publicacion_list'), 
    
    # Agregar nueva publicación (URL: /publicaciones/agregar/)
    path('agregar/', PublicacionCreateView.as_view(), name='publicacion_create'),
    
    # Editar publicación (URL: /publicaciones/editar/1/)
    path('editar/<int:pk>/', PublicacionUpdateView.as_view(), name='publicacion_update'),
    
    # Eliminar publicación (URL: /publicaciones/eliminar/1/)
    path('eliminar/<int:pk>/', PublicacionDeleteView.as_view(), name='publicacion_delete'),
]