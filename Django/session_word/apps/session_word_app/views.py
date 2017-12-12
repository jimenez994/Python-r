from django.shortcuts import render, redirect
from time import gmtime, strftime
def index(request):
    if 'arr' not in request.session:
        request.session['arr'] = []
    print request.session['arr']
    return render(request, "session_word_app/index.html")

def add_word(request):
    name = request.POST["name"]
    color = request.POST["color"]
    font = 16
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    # request.POST["font"] 
    if len(name) < 1:
        return redirect("/")
    if 'font' in request.POST:
        font = 24
    
    mylist = {
        'name': name, 
        'color': color, 
        'font': font,
        'time': time,
    }

    temp = request.session['arr']
    temp.append(mylist)
    request.session['arr'] = temp
    return redirect("/")


def clear(request):
    request.session.clear()
    return redirect("/")
