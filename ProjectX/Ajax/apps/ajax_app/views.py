from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
import math

def index(request):
    users = User.objects.all()
    user_lists = []
    for user in range(0, int(math.ceil(len(users)/10))):
        user_lists.append(user+1)
    context = {
        'users': users[0:10],
        'user_lists': user_lists
    }

    return render(request, "ajax_app/index.html", context)

def create(request):
    User.objects.create(
        email=request.POST['email'],
        first_name = request.POST['first_name'],
        last_name=request.POST['last_name'],
    )
    return redirect('/')

