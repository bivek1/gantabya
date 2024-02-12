from django.shortcuts import render

# Create your views here.
def homepage(request):
    
    return render(request, "index.html")

def loginView(request):
    return render(request, "homepage/login.html")

def courseView(request):
    return render(request, "homepage/course.html")

def contactView(request):
    return render(request, "homepage/contact.html")

def aboutView(request):
    return render(request, "homepage/about.html")