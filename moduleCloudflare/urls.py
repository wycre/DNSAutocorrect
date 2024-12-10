from django.urls import path, include
from . import views

urlpatterns = [
    path('new_service/', views.new_cloudflare_service, name='new_cloudflare_service'),
    path('edit_service/', views.edit_cloudflare_service, name='edit_cloudflare_service'),
    path('delete_service/', views.delete_cloudflare_service, name='delete_cloudflare_service'),
]