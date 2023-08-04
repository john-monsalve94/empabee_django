from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoReporteColmena.as_view(
        template_name="ReporteColmena/index.html"), name='tablaReporteColmena'),
    path('detalle/<int:pk>', ReporteColmenaDetalle.as_view(
        template_name="ReporteColmena/detalle.html"), name='detalleReporteColmena'),
    path('editar/<int:pk>', ReporteColmenaActualizar.as_view(
        template_name="ReporteColmena/actualizar.html"), name='actualizarReporteColmena'),
    path('crear', ReporteColmenaCrear.as_view(
        template_name="ReporteColmena/crear.html"), name='crearReporteColmena'),
    path('eliminar/<int:pk>', ReporteColmenaEliminar.as_view(),
         name='ReporteColmena/eliminar.html')

]
