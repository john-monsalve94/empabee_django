from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoMSensorColmena.as_view(
        template_name="msensorColmena/index.html"), name='tablaMSC'),
    path('detalle/<int:pk>', MSensorColmenaDetalle.as_view(
        template_name="msensorColmena/detalle.html"), name='detalleMSC'),
    path('editar/<int:pk>', MSensorColmenaActualizar.as_view(
        template_name="msensorColmena/actualizar.html"), name='actualizarMSC'),
    path('crear', MSensorColmenaCrear.as_view(
        template_name="msensorColmena/crear.html"), name='crearMSC'),
    path('eliminar/<int:pk>', MSensorColmenaEliminar.as_view(),
         name='msensorColmena/eliminar.html')

]
