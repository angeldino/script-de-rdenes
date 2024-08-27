from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.register, name='home'),
    path('crear/', views.create_new_trip, name='create_new_trip'),
]