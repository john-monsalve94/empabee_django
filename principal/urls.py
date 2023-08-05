from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import login
from .views_templates import urls as view_urls

urlpatterns = [

    # rutas para las vistas de todos los cruds
    path('views_templates/', include(view_urls)),
    path('login/',LoginView.as_view(template_name='auth/login.html'),name='login'),
    
]
