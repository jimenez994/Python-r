from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return render(request, "bo_app/index.html")


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
        "all_users": User.objects.all(),
        "user": User.objects.get(id=request.session["user_id"]),
        "users": User.objects.all().exclude(id=request.session["user_id"]),
        "posts": Post.objects.order_by("-created_at").all(),
        "comments": Comment.objects.all(),
        "requests": Request.objects.filter(user_being_requested_id=request.session["user_id"]),
    }
    return render(request, "bo_app/home.html", context)

def post(request,id):
    new_post = Post.objects.posting(
    request.POST["post_content"],
    id
    )
    return redirect("/home")

def comment(request,post_id):
    new_comment = Comment.objects.commenting(
        request.POST["comment_content"],
        request.session["user_id"],
        post_id
    )
    return redirect("/home")

def request(request,id):
    Request.objects.create(
        user_being_requested_id = id,
        user_requesting_id = request.session["user_id"]
    )
    return redirect("/home")
