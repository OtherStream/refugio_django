from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')])
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='animales/', blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=[('En adopción', 'En adopción'), ('Adoptado', 'Adoptado')],
        default='En adopción'
    )

    def __str__(self):
        return self.nombre