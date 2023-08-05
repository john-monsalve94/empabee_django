from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoColmena.as_view(
        template_name="crud/colmena/tables.html"), name='tablaCol'),
    path('detalle/<int:pk>', ColmenaDetalle.as_view(
        template_name="crud/colmena/detalle.html"), name='detalleCol'),
    path('editar/<int:pk>', ColmenaActualizar.as_view(
        template_name="crud/colmena/actualizar.html"), name='actualizarCol'),
    path('crear', ColmenaCrear.as_view(
        template_name="crud/colmena/crear.html"), name='crearCol'),
    path('eliminar/<int:pk>', ColmenaEliminar.as_view(),
         name='crud/colmena/eliminar.html')

]
