# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Tratamiento as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoTratamiento(ListView):
    model = table


class TratamientoCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Tratamiento creado correctamente'

    def get_success_url(self):
        return reverse('tablaTratamiento')


class TratamientoDetalle (DetailView):
    model = table


class TratamientoActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Tratamiento Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTratamiento')


class TratamientoEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Tratamiento Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTratamiento')
