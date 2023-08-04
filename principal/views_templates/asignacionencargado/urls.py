from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoAsignacionEncargado.as_view(
        template_name="AsignacionEncargado/index.html"), name='tablaAsignacionEncargado'),
    path('detalle/<int:pk>', AsignacionEncargadoDetalle.as_view(
        template_name="AsignacionEncargado/detalle.html"), name='detalleAsignacionEncargado'),
    path('editar/<int:pk>', AsignacionEncargadoActualizar.as_view(
        template_name="AsignacionEncargado/actualizar.html"), name='actualizarAsignacionEncargado'),
    path('crear', AsignacionEncargadoCrear.as_view(
        template_name="AsignacionEncargado/crear.html"), name='crearAsignacionEncargado'),
    path('eliminar/<int:pk>', AsignacionEncargadoEliminar.as_view(),
         name='AsignacionEncargado/eliminar.html')

]
