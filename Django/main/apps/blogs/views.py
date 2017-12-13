from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(response):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(response):
    response = "create"
    return redirect('/blogs')
def show(request, number):
    print number 
    return HttpResponse("placeholder to display blog " + number)
def edit(request, number):
    print number 
    return HttpResponse("placeholder to edit blog " + number)
def destroy(request, number):
    print number
    return redirect('/blogs')
