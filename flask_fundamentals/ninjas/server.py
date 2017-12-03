from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")
@app.route("/ninja/<word>")
def ninja_color(word):
    print word
    if word == "blue":
        return render_template("ninja2.html")
    elif word == "red":
        return render_template("ninja4.html")
    elif word == "purple":
        return render_template("ninja1.html")
    elif word == "orange":
        return render_template("ninja3.html")
    else:
        return render_template("april.html")

app.run(debug=True)
