from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    errors = {}
    form_data = {}

    if request.method == 'POST':
        usuario = request.POST.get('usuario', '').strip()
        password = request.POST.get('password', '').strip()
        form_data['usuario'] = usuario

        if not usuario or not password:
            return redirect('/login/?error=empty')

        if usuario != 'admin' or password != '1234': 
            return redirect('/login/?error=invalid')

        return redirect('/dashboard/')  

    return render(request, 'usuarios/login.html', {'errors': errors, 'form_data': form_data})