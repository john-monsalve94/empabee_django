# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import InfotrataEstanque as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoInfotrataEstanque(ListView):
    model = table


class InfotrataEstanqueCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'InfotrataEstanque creado correctamente'

    def get_success_url(self):
        return reverse('tablaInfotrataEstanque')


class InfotrataEstanqueDetalle (DetailView):
    model = table


class InfotrataEstanqueActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'InfotrataEstanque Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaInfotrataEstanque')


class InfotrataEstanqueEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'InfotrataEstanque Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaInfotrataEstanque')
