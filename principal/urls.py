from django.urls import path,include
from .views_templates import urls as view_urls

urlpatterns = [
    
    #rutas para las vistas de todos los cruds
    path('views_templates/',include(view_urls)),

]