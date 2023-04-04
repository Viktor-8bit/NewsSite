"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from _NewsSite import views


urlpatterns = [
    path('admin/', admin.site.index),
    path('', views.index),
    path('reg/', views.registration_page),
    path('log/', views.login_page),
    path('create_post/', views.post_create_page),
    path('post/', views.post),
    path('post/category/', views.post_by_category),
    path('post/get_comments', views.get_comments)
]

