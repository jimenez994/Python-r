from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():
    name = request.form['name']
    last= request.form['last']
    print name
    return render_template('process.html', first_name = name,last_name = last)



app.run(debug=True)
