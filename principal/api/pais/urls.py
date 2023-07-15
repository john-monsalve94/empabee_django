from django.urls import path
from .responses import *

urlpatterns = [
    path('', listar_paises, name='listar_paises'),
    path('<int:id>/', obtener_pais, name='obtener_pais'),
    path('crear',crear_pais,name='crear_pais'),
    path('actualizar/<int:id>/',actualizar_pais,name="actualizar_pais"),
    path('eliminar/<int:id>/',eliminar_pais,name="eliminar_pais"),
]