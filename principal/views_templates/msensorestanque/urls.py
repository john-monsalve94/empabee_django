from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoMSensorEstanque.as_view(
        template_name="mmsensorEstanque/index.html"), name='tablaMSE'),
    path('detalle/<int:pk>', MSensorEstanqueDetalle.as_view(
        template_name="msensorEstanque/detalle.html"), name='detalleMSE'),
    path('editar/<int:pk>', MSensorEstanqueActualizar.as_view(
        template_name="msensorEstanque/actualizar.html"), name='actualizarMSensorEstanque'),
    path('crear', MSensorEstanqueCrear.as_view(
        template_name="msensorEstanque/crear.html"), name='crearMSensorEstanque'),
    path('eliminar/<int:pk>', MSensorEstanqueEliminar.as_view(),
         name='msensorEstanque/eliminar.html')

]
