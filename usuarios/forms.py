from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
