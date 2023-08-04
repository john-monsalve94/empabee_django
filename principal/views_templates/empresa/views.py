# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Empresa as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoEmpresa(ListView):
    model = table


class EmpresaCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Empresa creado correctamente'

    def get_success_url(self):
        return reverse('tablaEmpresa')


class EmpresaDetalle (DetailView):
    model = table


class EmpresaActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Empresa Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaEmpresa')


class EmpresaEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Empresa Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaEmpresa')
