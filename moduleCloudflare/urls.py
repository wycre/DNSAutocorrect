from django.urls import path, include
from . import views

urlpatterns = [
    path('new_service/', views.new_individual_service, name='new_cloudflare_service'),
    path('edit_service/', views.edit_individual_service, name='edit_cloudflare_service'),
]