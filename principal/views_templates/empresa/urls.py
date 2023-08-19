from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoEmpresa.as_view(
        template_name="crud/Empresa/tables.html"), name='tablaEmpresa'),
    path('detalle/<int:pk>', EmpresaDetalle.as_view(
        template_name="crud/Empresa/detalle.html"), name='detalleEmpresa'),
    path('editar/<int:pk>', EmpresaActualizar.as_view(
        template_name="crud/Empresa/actualizar.html"), name='actualizarEmpresa'),
    path('crear', EmpresaCrear.as_view(
        template_name="crud/Empresa/crear.html"), name='crearEmpresa'),
    path('eliminar/<int:pk>', EmpresaEliminar.as_view(),
         name='crud/Empresa/eliminar.html')

]
