from django.urls import path,include
from .pais import urls as pais_urls

urlpatterns = [
    
    #rutas para la tabla pais
    path('pais/',include(pais_urls)),
    
]