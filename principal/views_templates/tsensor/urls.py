from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoTsensor.as_view(
        template_name="tsensor/index.html"), name='tablaTs'),
    path('detalle/<int:pk>', TsensorDetalle.as_view(
        template_name="tsensor/detalle.html"), name='detalleTs'),
    path('editar/<int:pk>', TsensorActualizar.as_view(
        template_name="tsensor/actualizar.html"), name='actualizarTs'),
    path('crear', TsensorCrear.as_view(
        template_name="tsensor/crear.html"), name='crearTs'),
    path('eliminar/<int:pk>', TsensorEliminar.as_view(),
         name='tsensor/eliminar.html')

]
