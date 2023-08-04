# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import MSensorColmena as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoMSensorColmena(ListView):
    model = table


class MSensorColmenaCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'MSensorColmena creado correctamente'

    def get_success_url(self):
        return reverse('tablaMSensorColmena')


class MSensorColmenaDetalle (DetailView):
    model = table


class MSensorColmenaActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'MSensorColmena Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaMSensorColmena')


class MSensorColmenaEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'MSensorColmena Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaMSensorColmena')
