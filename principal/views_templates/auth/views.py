from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from principal.models import Persona


class RegistrarUsuario(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )


class RegistrarPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'p_nombre',
            's_nombre',
            'p_apellido',
            's_apellido',
            'genero',
            'telefono',
            'n_identificacion',
            'ciudad_residencia',
            'ciudad_nacimiento',
            't_identificacion'
        ]
