from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoProduccionEstanque.as_view(
        template_name="ProduccionEstanque/index.html"), name='tablaProduccionEstanque'),
    path('detalle/<int:pk>', ProduccionEstanqueDetalle.as_view(
        template_name="ProduccionEstanque/detalle.html"), name='detalleProduccionEstanque'),
    path('editar/<int:pk>', ProduccionEstanqueActualizar.as_view(
        template_name="ProduccionEstanque/actualizar.html"), name='actualizarProduccionEstanque'),
    path('crear', ProduccionEstanqueCrear.as_view(
        template_name="ProduccionEstanque/crear.html"), name='crearProduccionEstanque'),
    path('eliminar/<int:pk>', ProduccionEstanqueEliminar.as_view(),
         name='ProduccionEstanque/eliminar.html')

]
