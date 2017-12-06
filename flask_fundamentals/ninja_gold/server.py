from flask import Flask, render_template,redirect,session,request
import random 
app = Flask(__name__)
app.secret_key = "real madrid"
@app.route('/')
def index():
    if 'yourGold' not in session:
        session['yourGold'] = 0

    if 'activity' not in session:
        session['activity'] = []

    return render_template('index.html')



@app.route('/process_gold', methods= ['POST'])
def process():
    
    if request.form['location'] == "farm":
        goldEarn = random.randint(10,20)
        message = "Earn ${} from the {}!".format(goldEarn,request.form['location'])
        session['activity'].append(message)
        print session['activity']  
        print message
        session['yourGold'] += goldEarn
    if request.form['location'] == "cave":
        goldEarn = random.randint(5, 10)
        message = "Earn ${} from the {}!".format(goldEarn,request.form['location'])
        session['activity'].append(message)
        print message
        session['yourGold'] += goldEarn
    if request.form['location'] == "house":
        goldEarn = random.randint(2, 5)
        message = "Earn ${} from the {}!".format(goldEarn,request.form['location'])
        session['activity'].append(message)
        print message
        session['yourGold'] += goldEarn
    if request.form['location'] == "casino":
        goldEarn = random.randint(-50, 50)
        if goldEarn > 0:
            winlose = "Earn"
        else:
            winlose = "Lost"
        message = "{} ${} from the {}!".format(winlose,abs(goldEarn),request.form['location'])
        session['activity'].append(message)
        print message
        session['yourGold'] += goldEarn

    print session['yourGold']

    return redirect('/')







app.run(debug=True)
