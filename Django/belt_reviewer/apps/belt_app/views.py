from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def index(request):
    return render(request, "belt_app/index.html")


def register(request):
    response = User.objects.register(
        request.POST["first"],
        request.POST["last"],
        request.POST["username"],
        request.POST["email"],
        request.POST["dob"],
        request.POST["password"],
        request.POST["confirm"],
    )
    if response["valid"]:
        request.session["user_id"] = response["user"].id
        return redirect("/wall")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")


def login(request):
    response = User.objects.login(
        request.POST["email"],
        request.POST["password"]
    )
    if response["valid"]:
        request.session["user_id"] = response["user"].id
        return redirect("/wall")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")


def logout(request):
    request.session.clear()
    return redirect("/")
def home(request):
    return redirect("/wall")


def wall(request):
    if "user_id" not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session["user_id"]),
        "users": User.objects.all().exclude(id=request.session["user_id"])
    }
    return render(request, "belt_app/wall.html", context)


def newbook(request):
    return render(request, "belt_app/addbook.html")

def  add(request):
    return redirect("/wall")