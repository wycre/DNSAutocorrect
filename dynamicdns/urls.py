"""
URL configuration for django_project project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setup/', views.SetUpView.as_view(), name='setup'),
    path('run_dns_check/', views.run_dns_check, name='run_dns_check'),

    path('new_record/', views.new_monitored_record, name='new_record'),
    path('edit_record/', views.edit_monitored_record, name='edit_record'),
    path('delete_record/', views.delete_monitored_record, name='delete_record'),

    path('new_service/', views.new_service_chooser, name='new_service'),
]

