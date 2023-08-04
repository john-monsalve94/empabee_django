from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoCabezaFactura.as_view(
        template_name="CabezaFactura/index.html"), name='tablaCabezaFactura'),
    path('detalle/<int:pk>', CabezaFacturaDetalle.as_view(
        template_name="CabezaFactura/detalle.html"), name='detalleCabezaFactura'),
    path('editar/<int:pk>', CabezaFacturaActualizar.as_view(
        template_name="CabezaFactura/actualizar.html"), name='actualizarCabezaFactura'),
    path('crear', CabezaFacturaCrear.as_view(
        template_name="CabezaFactura/crear.html"), name='crearCabezaFactura'),
    path('eliminar/<int:pk>', CabezaFacturaEliminar.as_view(),
         name='CabezaFactura/eliminar.html')

]
