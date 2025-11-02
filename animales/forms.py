from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        # Seleccionamos los campos que el admin puede llenar
        fields = [
            'nombre', 
            'descripcion', 
            'imagen', 
            'tipo', 
            'tamano', 
            'color', 
            'genero'
        ]
        # Opcional: Ponemos etiquetas bonitas
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'imagen': 'Imagen',
            'tipo': 'Tipo (Perro/Gato)',
            'tamano': 'Tamaño',
            'color': 'Color',
            'genero': 'Género',
        }
        
    def __init__(self, *args, **kwargs):
        # Esto es para que los campos usen las clases de Bootstrap
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})