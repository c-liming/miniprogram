from django.shortcuts import render
from .models import *
# Create your views here.


def login_views(request):

    if request.method == "GET":
        return render(request, "login/html/login.html") 

    elif request.method == "POST":
        
        return render(request, "login/html/login.html")
