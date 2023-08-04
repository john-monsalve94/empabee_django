# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Ciudad as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoCiudad(ListView):
    model = table


class CiudadCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Ciudad creado correctamente'

    def get_success_url(self):
        return reverse('tablaCiudad')


class CiudadDetalle (DetailView):
    model = table


class CiudadActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Ciudad Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCiudad')


class CiudadEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Ciudad Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCiudad')
