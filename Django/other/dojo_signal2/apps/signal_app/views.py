from django.shortcuts import render,redirect
from .models import User, Message

def index(request):
	messages = Message.objects.all()
	return render(request, "signal_app/index.html", {"messages": messages})
def register(request):
	print request.POST
	User.objects.register(
		request.s
	)
	return redirect("/")


def login(request):
	print request.POST
	return redirect("/")
