from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoCiudad.as_view(
        template_name="ciudad/index.html"), name='tablaCiudad'),
    path('detalle/<int:pk>',
         CiudadDetalle.as_view(template_name="ciudad/detalle.html"), name='detalleCiudad'),
    path('editar/<int:pk>', CiudadActualizar.as_view(
        template_name="ciudad/actualizar.html"), name='actualizarCiudad'),
    path('crear', CiudadCrear.as_view(
        template_name="ciudad/crear.html"), name='crearCiudad'),
    path('eliminar/<int:pk>', CiudadEliminar.as_view(),
         name='ciudad/eliminar.html')

]
