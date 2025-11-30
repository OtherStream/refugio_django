from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['nombre', 'tipo', 'descripcion', 'imagen', 'fecha_termino'] 
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }