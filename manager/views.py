from django.shortcuts import render

# Create your views here.
def dashBoard(request):
    return render(request, "manager/dashboard.html")