from django.urls import path, include
from . import views

"""
MODIFY the name field in each url pattern to match the name of the provider
"""
urlpatterns = [
    path('new_service/', views.new_individual_service, name='new_template_service'),
    path('edit_service/', views.edit_individual_service, name='edit_template_service'),
    path('delete_service/', views.delete_individual_service, name='delete_template_service'),
]