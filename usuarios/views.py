from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')

        if not usuario or not password:
            return redirect('/login?error=empty')

        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            return redirect('/login?error=invalid')

    return render(request, 'usuarios/login.html')

def vista_registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, '¡Te has registrado exitosamente!')
            return redirect('login') 
    else:
        form = RegistroUsuarioForm()
        
    return render(request, 'usuarios/registro.html', {'form': form})