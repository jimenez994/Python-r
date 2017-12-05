from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/processdata',methods=["POST"])
def process():
    Name = request.form['name']
    Last = request.form['last']
    Location = request.form['location']
    Language = request.form['fav_language']
    Comment = request.form['comment_field']

    return render_template("result.html",name=Name,last=Last,location=Location,language=Language,comment=Comment)


app.run(debug=True)
