# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Tsensor as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoTsensor(ListView):
    model = table


class TsensorCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Tsensor creado correctamente'

    def get_success_url(self):
        return reverse('tablaTsensor')


class TsensorDetalle (DetailView):
    model = table


class TsensorActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Tsensor Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTsensor')


class TsensorEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Tsensor Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTsensor')
