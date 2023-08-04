from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoInfotrataColmena.as_view(
        template_name="infotrataColmena/index.html"), name='tablaInfC'),
    path('detalle/<int:pk>', InfotrataColmenaDetalle.as_view(
        template_name="infotrataColmena/detalle.html"), name='detalleInfC'),
    path('editar/<int:pk>', InfotrataColmenaActualizar.as_view(
        template_name="infotrataColmena/actualizar.html"), name='actualizarInfotrataColmena'),
    path('crear', InfotrataColmenaCrear.as_view(
        template_name="infotrataColmena/crear.html"), name='crearInfotrataColmena'),
    path('eliminar/<int:pk>', InfotrataColmenaEliminar.as_view(),
         name='infotrataColmena/eliminar.html')

]
