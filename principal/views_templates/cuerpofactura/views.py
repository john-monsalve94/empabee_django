# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import CuerpoFactura as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoCuerpoFactura(ListView):
    model = table


class CuerpoFacturaCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'CuerpoFactura creado correctamente'

    def get_success_url(self):
        return reverse('tablaCuerpoFactura')


class CuerpoFacturaDetalle (DetailView):
    model = table


class CuerpoFacturaActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'CuerpoFactura Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCuerpoFactura')


class CuerpoFacturaEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'CuerpoFactura Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCuerpoFactura')
