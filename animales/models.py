from django.db import models

class Animal(models.Model):
    ESTATUS_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('adoptado', 'Adoptado'),
    ]
    TIPO_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]
    TAMANO_CHOICES = [
        ('pequeño', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    ]
    GENERO_CHOICES = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]

    nombre = models.CharField(max_length=100)
    
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, null=True, blank=True)
    
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='animales_adopcion/', blank=True, null=True)
    estatus = models.CharField(max_length=10, choices=ESTATUS_CHOICES, default='activo')

    tamano = models.CharField(max_length=10, choices=TAMANO_CHOICES, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, null=True, blank=True)


    def __str__(self):
        return self.nombre