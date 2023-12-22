"""
URL configuration for ipl_match project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from ipl_teams import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about1, name='about1'),
    path('about2', views.about2, name='about2'),
    path('about3', views.about3, name='about3'),
    path('about4', views.about4, name='about4'),
    path('about5', views.about5, name='about5'),
    path('about6', views.about6, name='about6'),
    path('about7', views.about7, name='about7'),


]
