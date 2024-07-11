from django.urls import path
from . import views

urlpatterns = [
    path('zf/', views.zfEstatus, name='zfestatus'),
    path('daimler/', views.daimlerEstatus, name='daimlerestatus'),
]