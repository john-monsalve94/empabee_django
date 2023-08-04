from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoEspeciePez.as_view(
        template_name="EspeciePez/index.html"), name='tablaEspeciePez'),
    path('detalle/<int:pk>', EspeciePezDetalle.as_view(
        template_name="EspeciePez/detalle.html"), name='detalleEspeciePez'),
    path('editar/<int:pk>', EspeciePezActualizar.as_view(
        template_name="EspeciePez/actualizar.html"), name='actualizarEspeciePez'),
    path('crear', EspeciePezCrear.as_view(
        template_name="EspeciePez/crear.html"), name='crearEspeciePez'),
    path('eliminar/<int:pk>', EspeciePezEliminar.as_view(),
         name='EspeciePez/eliminar.html')

]
