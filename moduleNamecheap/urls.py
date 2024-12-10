from django.urls import path, include
from . import views

urlpatterns = [
    path('new_service/', views.new_namecheap_service, name='new_namecheap_service'),
    path('edit_service/', views.edit_namecheap_service, name='edit_namecheap_service'),
    path('delete_service/', views.delete_namecheap_service, name='delete_namecheap_service'),
]