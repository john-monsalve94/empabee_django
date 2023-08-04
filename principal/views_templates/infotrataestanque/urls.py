from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoInfotrataEstanque.as_view(
        template_name="infotrataEstanque/index.html"), name='tablaInfE'),
    path('detalle/<int:pk>', InfotrataEstanqueDetalle.as_view(
        template_name="infotrataEstanque/detalle.html"), name='detalleInfE'),
    path('editar/<int:pk>', InfotrataEstanqueActualizar.as_view(
        template_name="infotrataEstanque/actualizar.html"), name='actualizarInfE'),
    path('crear', InfotrataEstanqueCrear.as_view(
        template_name="infotrataEstanque/crear.html"), name='crearInfE'),
    path('eliminar/<int:pk>', InfotrataEstanqueEliminar.as_view(),
         name='infotrataEstanque/eliminar.html')

]
