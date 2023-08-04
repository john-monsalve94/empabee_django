from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoDireccion.as_view(
        template_name="direccion/index.html"), name='tablaDireccion'),
    path('detalle/<int:pk>', DireccionDetalle.as_view(
        template_name="direccion/detalle.html"), name='detalleDireccion'),
    path('editar/<int:pk>', DireccionActualizar.as_view(
        template_name="direccion/actualizar.html"), name='actualizarDireccion'),
    path('crear', DireccionCrear.as_view(
        template_name="direccion/crear.html"), name='crearDireccion'),
    path('eliminar/<int:pk>', DireccionEliminar.as_view(),
         name='direccion/eliminar.html')

]
