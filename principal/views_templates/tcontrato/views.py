# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import TContrato as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoTContrato(ListView):
    model = table


class TContratoCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'TContrato creado correctamente'

    def get_success_url(self):
        return reverse('tablaTContrato')


class TContratoDetalle (DetailView):
    model = table


class TContratoActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'TContrato Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTContrato')


class TContratoEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'TContrato Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTContrato')
