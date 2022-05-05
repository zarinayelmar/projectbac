"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',views.home, name="home"),
    path('urum/',views.urum,name="urum"),
    path('send/',send_message),
    path('register/',views.register,name="register"),
    path('login/',views.LoginUser.as_view(),name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('makal/',views.makal,name="makal"),
    path('create/',views.create,name="create"),
    path('<int:pk>', views.NewsDetailView.as_view(), name="news-detail"),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name="news-update"),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name="news-delete")
]