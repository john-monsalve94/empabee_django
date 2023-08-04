from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoContrato.as_view(
        template_name="contrato/index.html"), name='tablaCont'),
    path('detalle/<int:pk>', ContratoDetalle.as_view(
        template_name="contrato/detalle.html"), name='detalleCont'),
    path('editar/<int:pk>', ContratoActualizar.as_view(
        template_name="contrato/actualizar.html"), name='actualizarCont'),
    path('crear', ContratoCrear.as_view(
        template_name="contrato/crear.html"), name='crearCont'),
    path('eliminar/<int:pk>', ContratoEliminar.as_view(),
         name='contrato/eliminar.html')

]
