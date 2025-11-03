# productos/forms.py

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # Campos que el admin podrá llenar
        fields = [
            'nombre', 
            'categoria',
            'descripcion', 
            'precio',
            'imagen', 
            'disponible'
        ]
        labels = {
            'nombre': 'Nombre del Producto',
            'categoria': 'Categoría',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'imagen': 'Imagen',
            'disponible': 'Disponible'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicamos la clase de Bootstrap a todos los campos
        for field_name, field in self.fields.items():
            # Excepto al checkbox 'disponible'
            if field_name != 'disponible':
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-check-input'})