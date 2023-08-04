# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import TEmpresa as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoTEmpresa(ListView):
    model = table


class TEmpresaCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'TEmpresa creado correctamente'

    def get_success_url(self):
        return reverse('tablaTEmpresa')


class TEmpresaDetalle (DetailView):
    model = table


class TEmpresaActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'TEmpresa Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTEmpresa')


class TEmpresaEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'TEmpresa Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaTEmpresa')
