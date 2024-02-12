from django.urls import path
from .import views

app_name = 'landing'

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('login', views.loginView, name="login"),
    path('course', views.courseView, name="course"),
    path('about', views.aboutView, name="about"),
    path('contact', views.contactView, name="contact"),
   
]
