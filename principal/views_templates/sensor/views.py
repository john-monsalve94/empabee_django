# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Sensor as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoSensor(ListView):
    model = table


class SensorCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Sensor creado correctamente'

    def get_success_url(self):
        return reverse('tablaSensor')


class SensorDetalle (DetailView):
    model = table


class SensorActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Sensor Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaSensor')


class SensorEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Sensor Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaSensor')
