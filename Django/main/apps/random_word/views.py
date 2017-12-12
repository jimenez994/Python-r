from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 1
    else: 
        request.session['counter'] += 1
    
    context = {
        "word": get_random_string(length=14)
    }

    return render(request, "random_word/index.html", context)

def random(response):
    
    response = "nice"
    return redirect("/random_word")
def reset(request):
    request.session['counter'] = 0
    return redirect("/random_word")

