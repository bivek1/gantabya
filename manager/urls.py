from django.urls import path
from .import views

app_name = 'manager'

urlpatterns = [
    path('dashboard', views.dashBoard, name = 'dashboard')
]