from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
import os


def index(request):
    return render(request, "wall_app/index.html")


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
        return redirect("/home")
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
        return redirect("/home")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")


def logout(request):
    request.session.clear()
    return redirect("/")


def home(request):
    if "user_id" not in request.session:
        return redirect("/")
    context = {
        "currentUser": User.objects.get(id=request.session["user_id"]),
        "posts": Post.objects.order_by("-created_at").all(),
    }
    return render(request, "wall_app/home.html", context)

def post(request):
    if len(request.POST["post"]) > 5:
        Post.objects.create(
            content=request.POST["post"],
            post_by_id=request.session["user_id"]
        )
        return redirect("/home")
    else:
        return redirect("/home")


def comment(request, post_id):
    new_comment = Comment.objects.commenting(
        request.POST["comment"],
        request.session["user_id"],
        post_id
    )
    return redirect("/home")
