from flask import Flask, render_template,request,redirect,session
from random import randint
app = Flask(__name__)
app.secret_key = "real madrid"


@app.route('/',methods=['POST','GET'])
def index():
    session['target'] = randint(0, 101)
    print session['target']
    
    return render_template('index.html')
    
@app.route('/guess', methods=['POST'])
def guess():
    
    if request.form['number'] != "":
        print "Im thinkng ",session['target']
        numberG = request.form['number']
        print "my number", numberG
        
        if int(numberG) == session['target']:
            return render_template('index.html',answer = ""+str(session['target'])+" That's my number!")
        elif int(numberG) > session['target']:
            return render_template('index.html', answer="That's too high")
        elif int(numberG) < session['target']:
            return render_template('index.html', answer="That's too low")
        
        else:
            print "thats not"
    else:
        return redirect("/")
@app.route('/play', methods=['POST'])
def play():
    print "is working"
    session['target'] = randint(0, 101)
    return render_template('index.html', answer="try your best guess")











app.run(debug=True)
