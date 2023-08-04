# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Estanque as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoEstanque(ListView):
    model = table


class EstanqueCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Estanque creado correctamente'

    def get_success_url(self):
        return reverse('tablaEstanque')


class EstanqueDetalle (DetailView):
    model = table


class EstanqueActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Estanque Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaEstanque')


class EstanqueEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Estanque Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaEstanque')
