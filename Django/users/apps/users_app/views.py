from django.shortcuts import render, redirect


def index(request):
    return render(request, "users_app/index.html")