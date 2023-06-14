from django.shortcuts import render
from principal.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages 

# Create your views here.
def Home(request):
    
    return render (request, "index.html")

def Parametros (request):
    return render (request, "crud/index.html")  

def Login(request):
    return render (request, "login.html")


 #-----------------------------------Apicultura-----------------------------------------------------#
class ListadoApicultura(CreateView,ListView,SuccessMessageMixin):

    model = Apicultura
    form = Apicultura
    fields = "__all__"
    
    success_message ='Apicultura creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer' 
    
class ApiculturaDetalle (DetailView):
    model =Apicultura

class ApiculturaActualizar(SuccessMessageMixin,UpdateView):
    model =Apicultura
    form = Apicultura
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Apicultura' de nuestra Base de Datos 
    success_message = 'Apicultura Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer') # Redireccionamos a la vista principal 'leer'
    
class ApiculturaEliminar(SuccessMessageMixin, DeleteView): 
    model = Apicultura
    form = Apicultura
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Apicultura Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer'
    
    #-----------------------------------Apicultura-----------------------------------------------------#