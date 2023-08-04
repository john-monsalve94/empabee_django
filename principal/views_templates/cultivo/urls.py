from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoCultivo.as_view(
        template_name="cultivo/index.html"), name='tablaCul'),
    path('detalle/<int:pk>', CultivoDetalle.as_view(
        template_name="cltivo/detalle.html"), name='detalleCul'),
    path('editar/<int:pk>', CultivoActualizar.as_view(
        template_name="cultivo/actualizar.html"), name='actualizarCult'),
    path('crear', CultivoCrear.as_view(
        template_name="cultivo/crear.html"), name='crearCul'),
    path('eliminar/<int:pk>', CultivoEliminar.as_view(),
         name='cultivo/eliminar.html')

]
