from django.contrib.auth.decorators import login_required 
from django.urls import path
from .views import *


urlpatterns = [

    path('', login_required(ListadoColmena.as_view(
        template_name="colmena/index.html")), name='tablaCol'),
    path('detalle/<int:pk>',login_required(ColmenaDetalle.as_view(
        template_name="colmena/detalle.html")), name='detalleCol'),
    path('editar/<int:pk>', login_required(ColmenaActualizar.as_view(
        template_name="colmena/actualizar.html")), name='actualizarCol'),
    path('crear',login_required(ColmenaCrear.as_view(
        template_name="colmena/crear.html")), name='crearCol'),
    path('eliminar/<int:pk>',login_required(ColmenaEliminar.as_view()),
         name='colmena/eliminar.html')

]
