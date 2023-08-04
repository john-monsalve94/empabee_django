from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoTEmpresa.as_view(
        template_name="tempresa/index.html"), name='tablaTEm'),
    path('detalle/<int:pk>', TEmpresaDetalle.as_view(
        template_name="tempresa/detalle.html"), name='detalleTEm'),
    path('editar/<int:pk>', TEmpresaActualizar.as_view(
        template_name="tempresa/actualizar.html"), name='actualizarTEm'),
    path('crear', TEmpresaCrear.as_view(
        template_name="tempresa/crear.html"), name='crearTEm'),
    path('eliminar/<int:pk>', TEmpresaEliminar.as_view(),
         name='tempresa/eliminar.html')

]
