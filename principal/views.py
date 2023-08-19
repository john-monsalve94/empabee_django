# Librerias del crud
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from principal.models import Persona
from principal.views_templates.auth.views import RegistrarPersona, RegistrarUsuario


def home(request):
    return render(request, 'home/index.html')

# pantalla de registro


def register(request: HttpRequest):
    data = {
        'usuario_form': RegistrarUsuario(),
        'persona_form': RegistrarPersona()
    }
    
    if request.method == 'POST':
        usuario_form: RegistrarUsuario = RegistrarUsuario(request.POST)
        persona_form: RegistrarPersona = RegistrarPersona(request.POST)
        if usuario_form.is_valid() and persona_form.is_valid():
            user: User = usuario_form.save()
            persona: Persona = persona_form.save(commit=False)
            persona.user = user
            persona.correo = user.email
            persona.save()

            user = authenticate(
                username=user.username,
                password=user.password
            )
            login(request, user)
        else:
                print("EL ESTADO DE USER",usuario_form.is_valid())
                print("EL ESTADO DE PERSONA",persona_form.is_valid())
    
 
    
    return render(request, 'auth/register.html', data)


# pantalla de inicio luego de iniciar sesión
@login_required
def dashboard(request):
    return render(request, 'crud/index.html')
