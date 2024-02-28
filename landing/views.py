from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def homepage(request):
    
    return render(request, "index.html")

def loginView(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user_get = authenticate(request, username = username, password=password)

        if user_get != None:
            login(request, user_get)
            return HttpResponseRedirect(reverse('manager:dashboard'))
            
        else:
            pass
            
        
    return render(request, "homepage/login.html")

def courseView(request):
    course = Course.objects.all()

    dist ={
        'course':course
    }
    
    return render(request, "homepage/course.html", dist)

def courseDetailView(request, slug):
    course = Course.objects.get(slug = slug)

    dist={
        'course':course
    }
    return render(request, "homepage/courseDetails.html", dist)

def contactView(request):
    return render(request, "homepage/contact.html")

def aboutView(request):
    return render(request, "homepage/about.html")

def signupView(request):
    return render(request, "homepage/signup.html")