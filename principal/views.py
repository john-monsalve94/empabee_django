#Librerias del crud
from django.shortcuts import render

# Create your views here.

#pantalla principal
def Home(request):
    return render(request,'index.html')

#pantalla de login
def Login(request):
    return render(request,'login.html')

#pantalla de registro
def Register(request):
    return render(request,'register.html')


#  #-----------------------------------Colmena-----------------------------------------------------#
# class ListadoColmena(CreateView,ListView,SuccessMessageMixin):

#     model = Colmena
#     form = Colmena
#     fields = "__all__"
    
#     success_message ='Colmena creado correctamente'
#     def get_success_url(self):        
#         return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer' 
    
# class ColmenaDetalle (DetailView):
#     model =Colmena

# class ColmenaActualizar(SuccessMessageMixin,UpdateView):
#     model =Colmena
#     form = Colmena
#     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Colmena' de nuestra Base de Datos 
#     success_message = 'Colmena Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

#     def get_success_url(self):               
#         return reverse('principal:leer') # Redireccionamos a la vista principal 'leer'
    
# class ColmenaEliminar(SuccessMessageMixin, DeleteView): 
#     model = Colmena
#     form = Colmena
#     fields = "__all__"     
 
#     # Redireccionamos a la página principal luego de eliminar un registro o postre
#     def get_success_url(self): 
#         success_message = 'Colmena Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
#         messages.success (self.request, (success_message))       
#         return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer'
    
#     #-----------------------------------Colmena-----------------------------------------------------#