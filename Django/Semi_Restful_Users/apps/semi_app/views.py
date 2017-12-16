from django.shortcuts import render,redirect
from .models import User


def index(request):
    users = User.objects.all()

    return render(request,"semi_app/index.html",{"users": users})


def edit(request,id):
    users = User.objects.get(id=id)
    return render(request, "semi_app/edit.html", {"users":users})

def update(request,id):
    user = User.objects.get(id=id)
    user.name = request.POST["name"]
    user.save()
    return redirect("/")
def new(request):
        
    return render(request, "semi_app/new.html")
def create(request):
    User.objects.create(
        name=request.POST["name"],
        email=request.POST["email"]

    )
    return redirect("/")

def info(request,id):
    users = User.objects.get(id=id)
    return render(request, "semi_app/info.html", {"users":users})

def delete(request,id):
    User.objects.get(id=id).delete()
    return redirect("/")
