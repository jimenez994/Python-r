from django.shortcuts import render, redirect
from random import randrange
def index(request):
    if 'yourGold' not in request.session:
        request.session['yourGold'] =  0
    if 'activity' not in request.session:
        request.session['activity'] = []

    return render(request, "ninja_gold_app/index.html")

def process_gold(request, location):
    print location
    if location == "farm":
        gold = randrange(10,21)
        
    elif location == "cave":
        gold = randrange(5,11)
    elif location == "house":
        gold = randrange(2,6)
    elif location == "casino":
        gold = randrange(-50,51)
    if gold >= 0:
         message = {
             "lost": False,
             "message": 'you went to the {} and earned {} gold'.format(location, gold)
         }
    else:
         message = {
             "lost": True,
             "message": 'you went to the {} and lost {} gold'.format(location, gold)
         }
   

    request.session['activity'].append(message)
        
    request.session['yourGold'] += gold
    return redirect('/')
