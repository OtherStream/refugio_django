# animales/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('adoptar/', views.lista_animales_adoptar, name='adoptar'),
    path('animal/crear/', views.gestionar_animal_view, name='animal_crear'),
    path('animal/editar/<int:pk>/', views.gestionar_animal_view, name='animal_editar'),
]