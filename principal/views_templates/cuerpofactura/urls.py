from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoCuerpoFactura.as_view(
        template_name="CuerpoFactura/index.html"), name='tablaCuerpoFactura'),
    path('detalle/<int:pk>', CuerpoFacturaDetalle.as_view(
        template_name="CuerpoFactura/detalle.html"), name='detalleCuerpoFactura'),
    path('editar/<int:pk>', CuerpoFacturaActualizar.as_view(
        template_name="CuerpoFactura/actualizar.html"), name='actualizarCuerpoFactura'),
    path('crear', CuerpoFacturaCrear.as_view(
        template_name="CuerpoFactura/crear.html"), name='crearCuerpoFactura'),
    path('eliminar/<int:pk>', CuerpoFacturaEliminar.as_view(),
         name='CuerpoFactura/eliminar.html')

]
