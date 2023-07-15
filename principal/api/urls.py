from django.urls import path,include
from .pais import urls as pais_urls

urlpatterns = [
    
    #rutas para la api
    path('pais/',include(pais_urls)),

]