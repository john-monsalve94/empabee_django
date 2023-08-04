# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import ProduccionEstanque as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoProduccionEstanque(ListView):
    model = table


class ProduccionEstanqueCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'ProduccionEstanque creado correctamente'

    def get_success_url(self):
        return reverse('tablaProduccionEstanque')


class ProduccionEstanqueDetalle (DetailView):
    model = table


class ProduccionEstanqueActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'ProduccionEstanque Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaProduccionEstanque')


class ProduccionEstanqueEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'ProduccionEstanque Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaProduccionEstanque')
