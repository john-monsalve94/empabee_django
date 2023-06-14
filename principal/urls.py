
from django.urls import path
from .views import *


urlpatterns = [
    
path('parametro/',Parametros, name='leerpar'),
#--------------------------------------------URL Apicultura ------------------------------------------------------------------------#
    
path('Apicultura/', ListadoApicultura.as_view(template_name = "crud/Apicultura/tables.html"), name='leerre'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
path('Apicultura/detalle/<int:pk>', ApiculturaDetalle.as_view(template_name = "crud/Apicultura/detalle.html"), name='detallesre'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Apicultura/editar/<int:pk>', ApiculturaActualizar.as_view(template_name = "crud/Apicultura/actualizar.html"), name='actualizarre'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Apicultura/eliminar/<int:pk>', ApiculturaEliminar.as_view(), name='crud/Apicultura/eliminar.html'),     
 #--------------------------------------------URL Apicultura ------------------------------------------------------------------------#
  
   
]