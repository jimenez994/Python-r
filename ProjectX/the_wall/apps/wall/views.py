from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, "wall/index.html")

def login(request):
    print request.POST
    user_list = User.objects.filter(username=username)
        if len(user_list) > 0
            User.objects.create(
                username = request.POST["username"]
            )
        else:
            
    return redirect("/dashboard")

def dashboard(request):
    return render(request, "wall/dashboard.html")
