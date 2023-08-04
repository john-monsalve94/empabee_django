# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import EspecieAbeja as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoEspecieAbeja(ListView):
    model = table


class EspecieAbejaCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'EspecieAbeja creado correctamente'

    def get_success_url(self):
        return reverse('tablaEspecieAbeja')


class EspecieAbejaDetalle (DetailView):
    model = table


class EspecieAbejaActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'EspecieAbeja Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaEspecieAbeja')


class EspecieAbejaEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'EspecieAbeja Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaEspecieAbeja')
