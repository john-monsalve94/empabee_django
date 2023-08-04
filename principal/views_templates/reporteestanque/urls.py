from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoReporteEstanque.as_view(
        template_name="ReporteEstanque/index.html"), name='tablaReporteEstanque'),
    path('detalle/<int:pk>', ReporteEstanqueDetalle.as_view(
        template_name="ReporteEstanque/detalle.html"), name='detalleReporteEstanque'),
    path('editar/<int:pk>', ReporteEstanqueActualizar.as_view(
        template_name="ReporteEstanque/actualizar.html"), name='actualizarReporteEstanque'),
    path('crear', ReporteEstanqueCrear.as_view(
        template_name="ReporteEstanque/crear.html"), name='crearReporteEstanque'),
    path('eliminar/<int:pk>', ReporteEstanqueEliminar.as_view(),
         name='ReporteEstanque/eliminar.html')

]
