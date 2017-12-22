from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Document


def home(request):
    documents = Document.objects.all()
    return render(request, 'upload_app/home.html', { 'documents': documents })

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload_app/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload_app/simple_upload.html')