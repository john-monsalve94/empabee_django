# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Colmena as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoColmena(ListView):
    model = table


class ColmenaCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Colmena creado correctamente'

    def get_success_url(self):
        return reverse('tablaCol')


class ColmenaDetalle (DetailView):
    model = table


class ColmenaActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Colmena Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCol')


class ColmenaEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Colmena Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaCol')
