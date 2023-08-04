from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoTContrato.as_view(
        template_name="TContrato/index.html"), name='tablaTContrato'),
    path('detalle/<int:pk>', TContratoDetalle.as_view(
        template_name="TContrato/detalle.html"), name='detalleTContrato'),
    path('editar/<int:pk>', TContratoActualizar.as_view(
        template_name="TContrato/actualizar.html"), name='actualizarTContrato'),
    path('crear', TContratoCrear.as_view(
        template_name="TContrato/crear.html"), name='crearTContrato'),
    path('eliminar/<int:pk>', TContratoEliminar.as_view(),
         name='TContrato/eliminar.html')

]
