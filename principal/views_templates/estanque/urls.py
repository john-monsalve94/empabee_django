from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoEstanque.as_view(
        template_name="estanque/index.html"), name='tablaEst'),
    path('detalle/<int:pk>', EstanqueDetalle.as_view(
        template_name="estanque/detalle.html"), name='detalleEst'),
    path('editar/<int:pk>', EstanqueActualizar.as_view(
        template_name="estanque/actualizar.html"), name='actualizarEst'),
    path('crear', EstanqueCrear.as_view(
        template_name="estanque/crear.html"), name='crearEst'),
    path('eliminar/<int:pk>', EstanqueEliminar.as_view(),
         name='estanque/eliminar.html')

]
