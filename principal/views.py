# Librerias del crud
from django.shortcuts import render
# Create your views here.

# pantalla principal


def Home(request):
    return render(request, 'crud/index.html')


# def Parametros(request):
#     return render(request, "index.html")

# pantalla de login


def Login(request):
    return render(request, 'login.html')

# pantalla de registro


def Register(request):
    return render(request, 'register.html')

#  # -----------------------------------Colmena-----------------------------------------------------#


# class ListadoColmena(CreateView, ListView, SuccessMessageMixin):

#     model = Colmena
#     form = Colmena
#     fields = "__all__"

#     success_message = 'Colmena creado correctamente'

#     def get_success_url(self):
#         # Redireccionamos a la vista principal 'leer'
#         return reverse('principal:leerre')


# class ColmenaDetalle (DetailView):
#     model = Colmena


# class ColmenaActualizar(SuccessMessageMixin, UpdateView):
#     model = Colmena
#     form = Colmena
#     # Le decimos a Django que muestre todos los campos de la tabla 'Colmena' de nuestra Base de Datos
#     fields = "__all__"
#     # Mostramos este Mensaje luego de Editar un Postre
#     success_message = 'Colmena Actualizado Correctamente !'

#     def get_success_url(self):
#         # Redireccionamos a la vista principal 'leer'
#         return reverse('principal:leer')


# class ColmenaEliminar(SuccessMessageMixin, DeleteView):
#     model = Colmena
#     form = Colmena
#     fields = "__all__"

#     # Redireccionamos a la página principal luego de eliminar un registro o postre
#     def get_success_url(self):
#         # Mostramos este Mensaje luego de Editar un Postre
#         success_message = 'Colmena Eliminado Correctamente !'
#         messages.success(self.request, (success_message))
#         # Redireccionamos a la vista principal 'leer'
#         return reverse('principal:leerre')

#     # -----------------------------------Colmena-----------------------------------------------------#
