# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import ReporteColmena as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoReporteColmena(ListView):
    model = table


class ReporteColmenaCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'ReporteColmena creado correctamente'

    def get_success_url(self):
        return reverse('tablaReporteColmena')


class ReporteColmenaDetalle (DetailView):
    model = table


class ReporteColmenaActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'ReporteColmena Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaReporteColmena')


class ReporteColmenaEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'ReporteColmena Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaReporteColmena')
