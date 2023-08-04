# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Cultivo as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoCultivo(ListView):
    model = table


class CultivoCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Cultivo creado correctamente'

    def get_success_url(self):
        return reverse('tablaCultivo')


class CultivoDetalle (DetailView):
    model = table


class CultivoActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Cultivo Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCultivo')


class CultivoEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Cultivo Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCultivo')
