from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoAsignacionEncargado.as_view(
        template_name="crud/AsignacionEncargado/tables.html"), name='tablaAsignacionEncargado'),
    path('detalle/<int:pk>', AsignacionEncargadoDetalle.as_view(
        template_name="crud/AsignacionEncargado/detalle.html"), name='detalleAsignacionEncargado'),
    path('editar/<int:pk>', AsignacionEncargadoActualizar.as_view(
        template_name="crud/AsignacionEncargado/actualizar.html"), name='actualizarAsignacionEncargado'),
    path('crear', AsignacionEncargadoCrear.as_view(
        template_name="crud/AsignacionEncargado/crear.html"), name='crearAsignacionEncargado'),
    path('eliminar/<int:pk>', AsignacionEncargadoEliminar.as_view(),
         name='crud/AsignacionEncargado/eliminar.html')

]
