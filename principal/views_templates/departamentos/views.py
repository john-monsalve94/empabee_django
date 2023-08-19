# Librerias del crud
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# importo el modelo de la base de datos models.py
from principal.models import Departamentos as table

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


# vistas
class ListadoDepartamentos(ListView):
    model = table


class DepartamentosCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Departamentos creado correctamente'

    def get_success_url(self):
        return reverse('tablaDep')


class DepartamentosDetalle (DetailView):
    model = table


class DepartamentosActualizar(SuccessMessageMixin, UpdateView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Departamentos Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('tablaDep')


class DepartamentosEliminar(SuccessMessageMixin, DeleteView):
    model = table
    form = table
    fields = "__all__"
    success_message = 'Departamentos Eliminado Correctamente !'

    def get_success_url(self):
        return reverse('tablaDep')
