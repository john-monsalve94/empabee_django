from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoSensor.as_view(
        template_name="crud/sensor/tables.html"), name='tablaSen'),
    path('detalle/<int:pk>',
         SensorDetalle.as_view(template_name="crud/sensor/detalle.html"), name='detalleSen'),
    path('editar/<int:pk>', SensorActualizar.as_view(
        template_name="crud/sensor/actualizar.html"), name='actualizarSen'),
    path('crear', SensorCrear.as_view(
        template_name="crud/sensor/crear.html"), name='crearSen'),
    path('eliminar/<int:pk>', SensorEliminar.as_view(),
         name='crud/sensor/eliminar.html')

]
