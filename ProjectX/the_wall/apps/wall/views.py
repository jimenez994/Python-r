from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, "wall/index.html")

def login(request):
    username = ''
    if len(request.POST["username"]) > 5:
        username = request.POST["username"]  
        user_list = User.objects.filter(username=username)
        if len(user_list) <= 0:
            User.objects.create(
                username = request.POST["username"]
                )
            return redirect("/dashboard")
        else:
            user = user_list[0]
            request.session["user_id"] = user.id
            return redirect("/dashboard") 
    else:
        return redirect("/")    
    
def dashboard(request):
    if "user_id" not in request.session:
        return redirect("/")
    content = {
        "currentUser": User.objects.get(id= request.session["user_id"]),
        "posts": Post.objects.order_by("-created_at").all()
    }
    return render(request, "wall/dashboard.html", content)

def logout(request):
    request.session.clear()
    return redirect("/")

def post(request):
    if len(request.POST["post"]) > 5:
        Post.objects.create(
            content = request.POST["post"],
            post_by_id = request.session["user_id"]
        )
        return redirect("/dashboard")
    else:
        return redirect("/dashboard")

def comment(request, post_id):
    if len(request.POST["comment"]) > 5:
        Comment.objects.create(
            content = request.POST["comment"],
            comment_by_id = request.session["user_id"],
            comment_to_id = post_id
            )    
    return redirect("/dashboard")
        
    
