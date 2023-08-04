from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoTratamiento.as_view(
        template_name="tratamiento/index.html"), name='tablaTra'),
    path('detalle/<int:pk>', TratamientoDetalle.as_view(
        template_name="tratamiento/detalle.html"), name='detalleTra'),
    path('editar/<int:pk>', TratamientoActualizar.as_view(
        template_name="tratamiento/actualizar.html"), name='actualizarTra'),
    path('crear', TratamientoCrear.as_view(
        template_name="tratamiento/crear.html"), name='crearTra'),
    path('eliminar/<int:pk>', TratamientoEliminar.as_view(),
         name='tratamiento/eliminar.html')

]
