# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import TIdentificacion as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoTIdentificacion(ListView):
    model = table


class TIdentificacionCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'TIdentificacion creado correctamente'

    def get_success_url(self):
        return reverse('tablaTIdentificacion')


class TIdentificacionDetalle (DetailView):
    model = table


class TIdentificacionActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'TIdentificacion Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTIdentificacion')


class TIdentificacionEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'TIdentificacion Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTIdentificacion')
