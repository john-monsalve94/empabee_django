from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


urlpatterns = [
    
    path('', login_required(ListadoPais.as_view(template_name = "pais/index.html")), name='tablaPais'),
    path('detalle/<int:pk>', PaisDetalle.as_view(template_name = "pais/detalle.html"), name='detallePais'),
    path('editar/<int:pk>', PaisActualizar.as_view(template_name = "pais/actualizar.html"), name='actualizarPais'),   
    path('crear', PaisCrear.as_view(template_name = "pais/crear.html"), name='crearPais'),
    path('eliminar/<int:pk>', PaisEliminar.as_view(), name='pais/eliminar.html')

]