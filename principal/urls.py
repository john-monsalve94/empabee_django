from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import login
from .views_templates import urls as view_urls

urlpatterns = [

    # path('parametro/', Parametros, name='leerpar'),
    # rutas para las vistas de todos los cruds
    path('views_templates/', include(view_urls)),
]
