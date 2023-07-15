from django.urls import path,include
from .views_templates import urls as view_urls
from .api import urls as api_urls

urlpatterns = [
    
    #rutas para las vistas de todos los cruds
    path('views_templates/',include(view_urls)),
    #rutas para la api
    path('api/',include(api_urls)),

]