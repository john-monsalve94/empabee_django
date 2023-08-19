"""
URL configuration for ipycBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Login view y logoutView permiten hacer login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from principal.views import *
from principal import urls as principal_urls
from .schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='index'),
    path('dashboard',dashboard,name="dashboard"),
    path('mi_cuenta/',login,name='mi_cuenta'),
    path('login/',LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='auth/login.html'),name='logout'),
    path('principal/',include(principal_urls)),
    path('graphql',GraphQLView.as_view(graphiql=True, schema=schema))
]
