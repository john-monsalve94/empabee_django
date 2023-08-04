from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoProduccionColmena.as_view(
        template_name="ProduccionColmena/index.html"), name='tablaProduccionColmena'),
    path('detalle/<int:pk>', ProduccionColmenaDetalle.as_view(
        template_name="ProduccionColmena/detalle.html"), name='detalleProduccionColmena'),
    path('editar/<int:pk>', ProduccionColmenaActualizar.as_view(
        template_name="ProduccionColmena/actualizar.html"), name='actualizarProduccionColmena'),
    path('crear', ProduccionColmenaCrear.as_view(
        template_name="ProduccionColmena/crear.html"), name='crearProduccionColmena'),
    path('eliminar/<int:pk>', ProduccionColmenaEliminar.as_view(),
         name='ProduccionColmena/eliminar.html')

]
