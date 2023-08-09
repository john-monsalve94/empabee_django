#Librerias del crud
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#importo el modelo de la base de datos models.py
from principal.models import Pais as table

#Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin


#vistas
class ListadoPais(ListView):
    model = table

class PaisCrear(SuccessMessageMixin, CreateView):
    model = table
    form = table
    fields = "__all__"
    success_message ='Pais creado correctamente'
    
    def get_success_url(self):        
        return reverse('tablaPais')

class PaisDetalle (DetailView):
    model = table

class  PaisActualizar(SuccessMessageMixin,UpdateView):
    model =  table
    form = table
    fields = "__all__" 
    success_message = 'Pais Actualizado Correctamente !'

    def get_success_url(self):               
        return reverse('tablaPais')


class PaisEliminar(SuccessMessageMixin, DeleteView): 
    model = table 
    form = table
    fields = "__all__" 
    success_message = 'Pais Eliminado Correctamente !'    
 
    def get_success_url(self): 
        return reverse('tablaPais') 