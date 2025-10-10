from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_adoptados, name='lista_adoptados'),
    path('adoptar/<int:animal_id>/', views.adoptar, name='adoptar'),
]
