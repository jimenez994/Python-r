from django.shortcuts import render, redirect
from .models import *
import math

def index(request):
    

    return render(request, "ajax_app/index.html")

def create(request):
    User.objects.create(
        email=request.POST['email'],
        first_name = request.POST['first_name'],
        last_name=request.POST['last_name'],
    )

    return redirect('/')
