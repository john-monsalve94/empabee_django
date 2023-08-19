from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoEspecieAbeja.as_view(
        template_name="crud/EspecieAbeja/tables.html"), name='tablaEspecieAbeja'),
    path('detalle/<int:pk>', EspecieAbejaDetalle.as_view(
        template_name="crud/EspecieAbeja/detalle.html"), name='detalleEspecieAbeja'),
    path('editar/<int:pk>', EspecieAbejaActualizar.as_view(
        template_name="crud/EspecieAbeja/actualizar.html"), name='actualizarEspecieAbeja'),
    path('crear', EspecieAbejaCrear.as_view(
        template_name="crud/EspecieAbeja/crear.html"), name='crearEspecieAbeja'),
    path('eliminar/<int:pk>', EspecieAbejaEliminar.as_view(),
         name='crud/EspecieAbeja/eliminar.html')

]
