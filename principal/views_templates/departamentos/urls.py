from django.urls import path
from .views import *


urlpatterns = [

    path('', ListadoDepartamentos.as_view(
        template_name="crud/departamentos/tables.html"), name='tablaDep'),
    path('detalle/<int:pk>', DepartamentosDetalle.as_view(
        template_name="crud/departamentos/detalle.html"), name='detalleDep'),
    path('editar/<int:pk>', DepartamentosActualizar.as_view(
        template_name="crud/departamentos/actualizar.html"), name='actualizarDep'),
    path('crear', DepartamentosCrear.as_view(
        template_name="crud/departamentos/crear.html"), name='crearDep'),
    path('eliminar/<int:pk>', DepartamentosEliminar.as_view(),
         name='crud/departamentos/eliminar.html')

]
