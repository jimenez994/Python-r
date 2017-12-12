from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print request
    return render(request, "survey/index.html")

def process(request):
    #a way to keep track of # views 
    # try: 
    #     request.session['count'] += 1
    # except KeyError as e:
    #     print e
    #     request.session['count'] = 1

    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    
    request.session['name'] = request.POST["name"]
    request.session['dojolocation'] = request.POST["dojolocation"]
    request.session['favlang'] = request.POST["favlang"]
    request.session['text_field'] = request.POST["text_field"]

    
    return redirect("/result")

def result(request):
    return render(request, "survey/result.html")
