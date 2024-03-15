from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
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
            if user_get.user_type  == 'owner':
                return HttpResponseRedirect(reverse('manager:dashboard'))
            elif user_get.user_type  == 'customer':
                return HttpResponseRedirect(reverse('customer:dashboard'))
            else:
                return render(request, "homepage/login.html")
        else:
            messages.error(request,"Invalid credentials")
            
        
    return render(request, "homepage/login.html")


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing:login'))

def courseView(request):
    course = Course.objects.all()

    dist = {
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

    if request.method == 'POST':
        email = request.POST['email_user']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        try:
            CustomUser.objects.create_user(first_name = first_name, last_name=last_name,username = email, email = email, password = password, user_type = 'customer')
            messages.success(request, "Succesfully created an account")
            return HttpResponseRedirect(reverse('landing:login'))
        except Exception as e:
            messages.error(request, "Email is already registered")
        
        
    return render(request, "homepage/signup.html")