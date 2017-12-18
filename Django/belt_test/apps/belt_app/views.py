from django.shortcuts import render, redirect
from .models import *
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
    friends = Friend.objects.filter(me=request.session["user_id"])
    for friend in friends:
        friendsids.append(friend.friend_with_id)

    notfriends = set(usersids) - set(friendsids)

    nofriends_message = ""
    if friendsids == []:
        nofriends_message = "You don't have friends yet"
    context = {
        "user": User.objects.get(id=request.session["user_id"]),
        "users": User.objects.all().exclude(id=request.session["user_id"]),
        "friends": Friend.objects.filter(me=request.session["user_id"]),
        "notfriends":notfriends,
        "message":nofriends_message,
    }
    return render(request, "belt_app/home.html", context)

def info(request,id):
    context = {
        "user": User.objects.get(id=id),   
    }
    return render(request,"belt_app/info.html",context)
def add(request,id):
    Friend.objects.create(
        friend_with_id=id,
        me_id=request.session["user_id"]
    )
    return redirect("/home")

def remove(request,id):
    Friend.objects.filter(friend_with_id=id).filter(me_id=request.session["user_id"]).delete()
    return redirect("/home")
