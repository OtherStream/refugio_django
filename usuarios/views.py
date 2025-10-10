from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
