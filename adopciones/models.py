from django.db import models
from django.conf import settings
from animales.models import Animal 

class Adopcion(models.Model):
    # Esta ForeignKey ahora usa el modelo Animal importado de 'animales'
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

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="solicitudes"
    )
    
    # Esta ForeignKey ahora usa el modelo Animal importado de 'animales'
    animal = models.ForeignKey(
        Animal, 
        on_delete=models.CASCADE, 
        related_name="solicitudes"
    )
    
    aceptado = models.CharField(
        max_length=1, 
        choices=ESTADO_CHOICES, 
        default='P'
    )
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.usuario.username} por {self.animal.nombre}"