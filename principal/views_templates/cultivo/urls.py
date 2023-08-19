from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoCultivo.as_view(
        template_name="crud/cultivo/tables.html"), name='tablaCul'),
    path('detalle/<int:pk>', CultivoDetalle.as_view(
        template_name="crud/cultivo/detalle.html"), name='detalleCul'),
    path('editar/<int:pk>', CultivoActualizar.as_view(
        template_name="crud/cultivo/actualizar.html"), name='actualizarCul'),
    path('crear', CultivoCrear.as_view(
        template_name="crud/cultivo/crear.html"), name='crearCul'),
    path('eliminar/<int:pk>', CultivoEliminar.as_view(),
         name='crud/cultivo/eliminar.html')

]
