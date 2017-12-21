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
    usersids = []
    users = User.objects.all().exclude(id=request.session["user_id"]).order_by("first_name")
    for user in users:
        usersids.append(user.id)

    friendsids = []
    friends = Friend.objects.filter(current_user=request.session["user_id"])
    for friend in friends:
        friendsids.append(friend.friends_with_id)

    notfriends = set(usersids) - set(friendsids)
    nofriends_message = ""
    if friendsids == []:
        nofriends_message = "You don't have friends yet"
    
    context = {
        "all_users": User.objects.all(),
        "user": User.objects.get(id=request.session["user_id"]),
        "users": User.objects.all().exclude(id=request.session["user_id"]),
        "posts": Post.objects.order_by("-created_at").all(),
        "comments": Comment.objects.all(),
        "friends": Friend.objects.filter(current_user=request.session["user_id"]),
        "notfriends": notfriends,
        "message": nofriends_message,
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

def add(request,id):
    Friend.objects.create(
        friends_with_id=id,
        current_user_id=request.session["user_id"]
    )
    Friend.objects.create(
        friends_with_id=request.session["user_id"],
        current_user_id=id
    )
    return redirect("/home")
