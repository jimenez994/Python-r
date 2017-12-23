from django.shortcuts import render, redirect
from .models import *
from .forms import *

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    posts = Post.objects.all()
    return render(request,"upload_app/index.html",{'posts': posts})

def upload(request):
    form = imageForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('/')
 
    return render(request, 'upload_app/upload.html',{'form': form })
