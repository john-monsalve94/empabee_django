# Librerias del crud
from http.client import HTTPException
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

# pantalla principal


def home(request):
    return render(request, 'home/index.html')

# pantalla de login


def login(request):
    return redirect(request, 'login')

# pantalla de registro


def register(request):
    return render(request, 'auth/registrarse.html')

# pantalla de inicio luego de iniciar sesión


@login_required
def dashboard(request):
    return render(request, 'crud/index.html')
