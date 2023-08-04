from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoEspecieAbeja.as_view(
        template_name="EspecieAbeja/index.html"), name='tablaEspecieAbeja'),
    path('detalle/<int:pk>', EspecieAbejaDetalle.as_view(
        template_name="EspecieAbeja/detalle.html"), name='detalleEspecieAbeja'),
    path('editar/<int:pk>', EspecieAbejaActualizar.as_view(
        template_name="EspecieAbeja/actualizar.html"), name='actualizarEspecieAbeja'),
    path('crear', EspecieAbejaCrear.as_view(
        template_name="EspecieAbeja/crear.html"), name='crearEspecieAbeja'),
    path('eliminar/<int:pk>', EspecieAbejaEliminar.as_view(),
         name='EspecieAbeja/eliminar.html')

]
