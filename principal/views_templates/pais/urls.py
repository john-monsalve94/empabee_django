from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('', login_required(ListadoPais.as_view(
        template_name="crud/pais/tables.html")), name='tablaPais'),
    path('detalle/<int:pk>',
         PaisDetalle.as_view(template_name="crud/pais/detalle.html"), name='detallePais'),
    path('editar/<int:pk>', PaisActualizar.as_view(template_name="crud/pais/actualizar.html"),
         name='actualizarPais'),
    path('crear', PaisCrear.as_view(
        template_name="crud/pais/tables.html"), name='crearPais'),
    path('eliminar/<int:pk>', PaisEliminar.as_view(), name='crud/eliminarPais')

]
