from django.db import models
from django.utils import timezone

TIPO_PUBLICACION = [
    ('AVISO', 'Aviso'),
    ('NOTICIA', 'Noticia'),
    ('OTRO', 'Otro'),
]

class Publicacion(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Título/Nombre') 
    
    tipo = models.CharField(
        max_length=10, 
        choices=TIPO_PUBLICACION, 
        default='AVISO', 
        verbose_name='Tipo de Publicación'
    )
    
    descripcion = models.TextField(verbose_name='Descripción')
    
    imagen = models.ImageField(upload_to='publicaciones', null=True, blank=True, verbose_name='Imagen')
    
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Publicación')

    fecha_termino = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Término')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones (Avisos/Servicios)'
        ordering = ['-fecha_creacion'] 

    def __str__(self):
        return self.nombre