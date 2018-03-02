from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
import math

def index(request):
	users = User.objects.all()
	user_lists = []
	pages = []
	
	if(len(users) > 10):
		num = len(users) / 10
		for i in range(0, num):
			pages.append(i + 1)
		if(len(users) % 10 != 0):
			pages.append(len(pages)+1)

	context = {
		'users': users[0:10],
		'pages': pages
	}
	return render(request, "ajax_app/index.html", context)

def search(request, id):
	users = User.objects.filter(
		first_name__startswith=request.POST['search']
	)
	if request.POST['to']:
		users = users.filter(created_at__lte=request.POST['to'])

	if request.POST['from']:
		users = users.filter(created_at__gte=request.POST['from'])


	user_lists = []
	pages = []

	if(len(users) > 10):
		num = len(users) / 10
		for i in range(0, num):
			pages.append(i + 1)
		if(len(users) % 10 != 0):
			pages.append(len(pages) + 1)

	if int(id) == 0 :
		new_list = users[0:10]
	else:
		end = int(id)*10
		start = end-10
		new_list =  users[start:end]
	context = {
		'users2': new_list,
		'pages': pages
	}	
	return render(request, "ajax_app/search.html", context)

def create(request):
    if(len(request.POST['email']) or len(request.POST['first_name']) or len(request.POST['last_name']) > 2):
        User.objects.create(
            email=request.POST['email'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
        )
        message = "you successfully registered a new user"
        return render(request, "ajax_app/message.html", {"message": message})
    else:
        message = "sorry something went wrong"
        return render(request, "ajax_app/message.html", {"message": message})



