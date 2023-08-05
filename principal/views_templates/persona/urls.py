from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoPersona.as_view(
        template_name="crud/persona/tables.html"), name='tablaPersona'),
    path('detalle/<int:pk>', PersonaDetalle.as_view(
        template_name="crud/persona/detalle.html"), name='detallePersona'),
    path('editar/<int:pk>', PersonaActualizar.as_view(
        template_name="crud/persona/actualizar.html"), name='actualizarPersona'),
    path('crear', PersonaCrear.as_view(
        template_name="crud/persona/crear.html"), name='crearPersona'),
    path('eliminar/<int:pk>', PersonaEliminar.as_view(),
         name='crud/persona/eliminar.html')

]
