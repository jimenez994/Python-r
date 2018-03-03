from django.shortcuts import render, redirect

def index(request):
    return render(request, "chat_app/index.html")