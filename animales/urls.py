# animales/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ... (otras urls)
    
    # Esta es la URL para tu página
    path('adoptar/', views.lista_animales_adoptar, name='adoptar'),
]