# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import ReporteEstanque as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoReporteEstanque(ListView):
    model = table


class ReporteEstanqueCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'ReporteEstanque creado correctamente'

    def get_success_url(self):
        return reverse('tablaReporteEstanque')


class ReporteEstanqueDetalle (DetailView):
    model = table


class ReporteEstanqueActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'ReporteEstanque Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaReporteEstanque')


class ReporteEstanqueEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'ReporteEstanque Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaReporteEstanque')
