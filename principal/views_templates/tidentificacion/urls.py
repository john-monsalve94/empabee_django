from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoTIdentificacion.as_view(
        template_name="tidentificacion/index.html"), name='tablaTId'),
    path('detalle/<int:pk>', TIdentificacionDetalle.as_view(
        template_name="tidentificacion/detalle.html"), name='detalleTId'),
    path('editar/<int:pk>', TIdentificacionActualizar.as_view(
        template_name="tidentificacion/actualizar.html"), name='actualizarTId'),
    path('crear', TIdentificacionCrear.as_view(
        template_name="tidentificacion/crear.html"), name='crearTId'),
    path('eliminar/<int:pk>', TIdentificacionEliminar.as_view(),
         name='tidentificacion/eliminar.html')

]
