from django.db import models

class Animal(models.Model):
    # --- Choices para los campos 'select' ---
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

    # --- Tus campos existentes ---
    nombre = models.CharField(max_length=100)
    
    # Modificado para usar los CHOICES
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, null=True, blank=True)
    
    descripcion = models.TextField() # Lo dejé como obligatorio (sin null=True)
    imagen = models.ImageField(upload_to='animales_adopcion/', blank=True, null=True)
    estatus = models.CharField(max_length=10, choices=ESTATUS_CHOICES, default='activo')

    # --- Campos nuevos agregados ---
    tamano = models.CharField(max_length=10, choices=TAMANO_CHOICES, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.nombre