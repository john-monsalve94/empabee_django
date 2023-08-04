# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Direccion as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoDireccion(ListView):
    model = table


class DireccionCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Direccion creado correctamente'

    def get_success_url(self):
        return reverse('tablaDireccion')


class DireccionDetalle (DetailView):
    model = table


class DireccionActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Direccion Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaDireccion')


class DireccionEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Direccion Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaDireccion')
