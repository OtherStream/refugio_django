from django import forms
from .models import Adopcion

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ['nombre_adoptante', 'email', 'telefono']