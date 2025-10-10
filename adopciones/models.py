from django.db import models

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