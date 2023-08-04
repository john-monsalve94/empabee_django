from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoTiptrata.as_view(
        template_name="tiptrata/index.html"), name='tablaTiptr'),
    path('detalle/<int:pk>', TiptrataDetalle.as_view(
        template_name="tiptrata/detalle.html"), name='detalleTiptr'),
    path('editar/<int:pk>', TiptrataActualizar.as_view(
        template_name="tiptrata/actualizar.html"), name='actualizarTiptr'),
    path('crear', TiptrataCrear.as_view(
        template_name="tiptrata/crear.html"), name='crearTiptr'),
    path('eliminar/<int:pk>', TiptrataEliminar.as_view(),
         name='tiptrata/eliminar.html')

]
