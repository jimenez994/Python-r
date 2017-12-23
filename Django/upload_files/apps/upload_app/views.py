from django.shortcuts import render, redirect
from .models import *
from .forms import *


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    posts = Post.objects.all()
    return render(request,"upload_app/index.html",{'posts': posts})

def upload(request):
    form = imageForm(request.POST or None, request.FILES or None)
    if request.FILES.get('image') != None:
        if form.is_valid():
            post = form.save()
            post.image = request.FILES['image']
            file_type = post.image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'form': form,
                    'error_message': 'image must me jpg'
                }
                return render(request, 'upload_app/index.html',context)
            post.save()
            return redirect("/")
    else:
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = imageForm()
        return render(request, 'upload_app/upload.html',{'form': form})

