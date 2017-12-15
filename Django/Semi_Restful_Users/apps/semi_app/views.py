from django.shortcuts import render

def index(request):
    return render(request,"semi_app/index.html")
