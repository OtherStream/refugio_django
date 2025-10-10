from django.db import models

class usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo   = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'),('Otros','Otros')])
    usuario = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=20, default='usuario')

    def __str__(self):
        return self.nombre