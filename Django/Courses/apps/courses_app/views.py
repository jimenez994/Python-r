from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
def index(request):
    courses = Course.objects.all()
    message = messages.warning(request, 'Your account expires in three days.')
    return render(request,"courses_app/index.html",{"courses": courses,"message":message})

def add(request):
    response = Course.objects.register(
        request.POST["name"],
        request.POST["description"]
    )
    print response
    return redirect("/")
def remove(request,id):
    course = Course.objects.get(id=id)
    return render(request,"courses_app/destroy.html",{"course":course})

def delete(request,id):
    Course.objects.get(id=id).delete()
    return redirect("/")
