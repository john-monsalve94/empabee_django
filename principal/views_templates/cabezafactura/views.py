# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import CabezaFactura as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoCabezaFactura(ListView):
    model = table


class CabezaFacturaCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'CabezaFactura creado correctamente'

    def get_success_url(self):
        return reverse('tablaCabezaFactura')


class CabezaFacturaDetalle (DetailView):
    model = table


class CabezaFacturaActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'CabezaFactura Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCabezaFactura')


class CabezaFacturaEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'CabezaFactura Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCabezaFactura')
