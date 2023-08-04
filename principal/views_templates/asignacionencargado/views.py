# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import AsignacionEncargado as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoAsignacionEncargado(ListView):
    model = table


class AsignacionEncargadoCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'AsignacionEncargado creado correctamente'

    def get_success_url(self):
        return reverse('tablaAsignacionEncargado')


class AsignacionEncargadoDetalle (DetailView):
    model = table


class AsignacionEncargadoActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'AsignacionEncargado Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaAsignacionEncargado')


class AsignacionEncargadoEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'AsignacionEncargado Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaAsignacionEncargado')
