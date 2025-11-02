from django.db import models
from django.conf import settings
from animales.models import Animal 

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    raza = models.CharField(max_length=50)
    # otros campos que tengas en tu tabla

class Adopcion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    nombre_adoptante = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

class Solicitud(models.Model):
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('A', 'Aceptado'),
        ('R', 'Rechazado'),
    ]

    # Relación con el usuario que hace la solicitud
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="solicitudes"
    )
    
    # Relación con el animal que es solicitado
    animal = models.ForeignKey(
        Animal, 
        on_delete=models.CASCADE, 
        related_name="solicitudes"
    )
    
    # Estado de la solicitud
    aceptado = models.CharField(
        max_length=1, 
        choices=ESTADO_CHOICES, 
        default='P'
    )
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.usuario.username} por {self.animal.nombre}"