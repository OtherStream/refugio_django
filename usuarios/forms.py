from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class LoginForm(forms.Form):
    usuario = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
class RegistroUsuarioForm(UserCreationForm):
    
    first_name = forms.CharField(label='Nombre', max_length=150, required=True)
    last_name = forms.CharField(label='Apellidos', max_length=150, required=True)
    email = forms.EmailField(label='Email', required=True)
    telefono = forms.CharField(label='Teléfono', max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'Ej. 1234567890'}))
    direccion = forms.CharField(label='Dirección', max_length=255, required=False)
    edad = forms.IntegerField(label='Edad', required=False)
    sexo = forms.ChoiceField(label='Sexo', choices=Usuario.SEXO_CHOICES, required=False)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'telefono',
            'direccion',
            'edad',
            'sexo',
        )