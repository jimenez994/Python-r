from django.shortcuts import render, redirect

def index(request):

    return render(request, "amadom_app/index.html")
# Create your views here.


def checkout(request):

    return render(request, "amadom_app/checkout.html")
def process(request):
    shirttotal = 19.99 * float(request.POST['Qtshirt'])
    sweatertotal = 29.99 * float(request.POST['Qsweater'])
    cuptotal = 4.99 * float(request.POST['Qcup'])
    booktotal = 49.99 * float(request.POST['Qbook'])
    request.session['total'] = shirttotal + sweatertotal + cuptotal + booktotal

    totalspend = request.session['total']
    print totalspend
    request.session['totalspend'] += totalspend

    total = int(request.POST['Qtshirt']) + int(request.POST['Qsweater']) + int(request.POST['Qcup']) + int(request.POST['Qbook'])
    request.session['items'] += total 
    
    
    return redirect("/checkout")
def back(request):
    
    return redirect("/")

