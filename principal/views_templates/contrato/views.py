# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Contrato as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoContrato(ListView):
    model = table


class ContratoCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Contrato creado correctamente'

    def get_success_url(self):
        return reverse('tablaContrato')


class ContratoDetalle (DetailView):
    model = table


class ContratoActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Contrato Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaContrato')


class ContratoEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Contrato Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaContrato')
