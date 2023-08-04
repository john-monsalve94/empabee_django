# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import InfotrataColmena as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoInfotrataColmena(ListView):
    model = table


class InfotrataColmenaCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'InfotrataColmena creado correctamente'

    def get_success_url(self):
        return reverse('tablaInfotrataColmena')


class InfotrataColmenaDetalle (DetailView):
    model = table


class InfotrataColmenaActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'InfotrataColmena Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaInfotrataColmena')


class InfotrataColmenaEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'InfotrataColmena Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaInfotrataColmena')
