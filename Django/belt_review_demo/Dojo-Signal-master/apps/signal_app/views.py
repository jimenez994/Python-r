from django.shortcuts import render, redirect
from .models import User, Message,Friend
from django.contrib import messages

def index(request):
	return render(request, "signal_app/index.html")

def register(request):
	response = User.objects.register(
		request.POST["first"],
		request.POST["last"],
		request.POST["username"],
		request.POST["email"],
		request.POST["dob"],
		request.POST["password"],
		request.POST["confirm"]
	)
	print response
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

	context = {
		"user": User.objects.get(id=request.session["user_id"]),
		"users": User.objects.all().exclude(id=request.session["user_id"]).order_by("first_name"),
		
		"your_messages": Message.objects.filter(received_by=request.session["user_id"]),

		"friends": Friend.objects.filter(me=request.session["user_id"]),
	
		"notfriends":notfriends
	}

	return render(request, "signal_app/home.html", context)

def delete(request, id):
	Friend.objects.filter(friend_with_id=id).filter(me_id=request.session["user_id"]).delete()
	return redirect("/home")

def add(request, id):
	Friend.objects.create(
		friend_with_id=id,
		me_id=request.session["user_id"]
		)
	return redirect("/home")

def new_message(request, id):
	return render(request, "signal_app/new_message.html", {"id": id})

def add_message(request, id):
	new_message = Message.objects.sendMessage(
		request.POST["content"],
		request.session["user_id"],
		id
	)
	if type(new_message) is unicode:
		messages.add_message(request, messages.ERROR, new_message)
		return redirect("/message/" + str(id))
	else:
		return redirect("/home")

def view_messages(request):
	your_messages = Message.objects.filter(received_by=request.session["user_id"])
	store = [message for message in your_messages]
	
	return render(request, "signal_app/messages.html" ,{"your_messages": store})
