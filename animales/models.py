# animales/models.py

from django.db import models

class Animal(models.Model):
    ESTATUS_CHOICES = [
        ('activo', 'Activo'),     # Disponible para adopción
        ('inactivo', 'Inactivo'), # En proceso / Ya solicitado
        ('adoptado', 'Adoptado'),
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='animales_adopcion/', blank=True, null=True)
    estatus = models.CharField(max_length=10, choices=ESTATUS_CHOICES, default='activo')

    def __str__(self):
        return self.nombre