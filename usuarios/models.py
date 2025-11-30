from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    SEXO_CHOICES = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ]

    telefono = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.username