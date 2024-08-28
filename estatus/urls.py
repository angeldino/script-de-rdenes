from django.urls import path
from . import views

urlpatterns = [
    path('calculate_distance/', views.calculate_distance, name='calculate_distance'),
    path('', views.register, name='home'),
]   