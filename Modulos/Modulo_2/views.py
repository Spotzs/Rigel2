from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm
from Modulos.Modulo_1.models import Producto, Cliente


def landing(request):
    productos = Producto.objects.all()
    # registros_por_pagina = int(request.GET.get('registrosPorPagina', 5))  # Obtener el valor del parámetro GET, con 10 como valor predeterminado
    # paginator = Paginator(productos, registros_por_pagina)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {
        'productos': productos,
        # 'paginator': paginator,
        # 'page_obj': page_obj,
        # 'registros_por_pagina': registros_por_pagina,  # Agregar el valor de registros_por_pagina al contexto
    }
    return render(request, "landing.html", context)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            colegio = form.cleaned_data.get('colegio')
            tipo = form.cleaned_data.get('tipo')
            telefono = form.cleaned_data.get('telefono')  # Obtener el valor del campo "telefono"
            direccion = form.cleaned_data.get('direccion')  # Obtener el valor del campo "direccion"
            genero = form.cleaned_data.get('genero')  # Obtener el valor del campo "genero"
            cliente = Cliente(usuario=user, colegio=colegio, tipo=tipo, telefono=telefono, direccion=direccion, genero=genero)  # Guardar los valores de los campos adicionales
            cliente.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'login.html', {'registro_form': form})


from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige al usuario después del inicio de sesión exitoso
    else:
        login_form = AuthenticationForm()
    # Instancia del formulario de registro
    registro_form = SignUpForm()
    return render(request, 'login.html', {'login_form': login_form, 'registro_form': registro_form})
