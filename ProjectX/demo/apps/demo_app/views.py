from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.core import serializers 

def index(request):
    return render(request, "demo_app/index.html")

def create(request):
    if( len(request.POST['email']) or len(request.POST['first_name']) or len(request.POST['last_name']) > 2):
        User.objects.create(
            email = request.POST['email'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
        )
        users = User.objects.order_by("-id").all()
        return render(request, "demo_app/all.html", {"users": users})
    else:
        users = User.objects.order_by("-id").all()
        return render(request, "demo_app/all.html", {"users": users})

def all_json(request):
    users = User.objects.all()
    users_json = serializers.serialize('json', users)
    return HttpResponse(users_json, content_type='application/json')

def all_html(request):
    users = User.objects.all()
    return render(request, "demo_app/all.html", {"users": users})

def find(request):
    users = User.objects.filter(
        first_name__startswith=request.POST['first_name_starts_with'])
    
    return render(request, "demo_app/all.html", {"users": users})
