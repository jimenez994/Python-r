from flask import Flask, render_template, redirect, request, session, flash
from random import randrange
from test import Student

app = Flask(__name__)
app.secret_key = "could this key be any more secret"

TITLES = ["Hello Python", "'Sup", "Contents"]

@app.route("/")
def index():
	title = TITLES[randrange(len(TITLES))]
	return render_template("index.html", title=title)

@app.route("/home")
def home():
	student1 = Student("slim shady")
	student1.introduce()
	return render_template("home.html")

@app.route("/process", methods=["POST"])
def process():
	
	errors = []

	if len(request.form["name"]) < 1:
		errors.append("Name is required")
	if len(request.form["email"]) < 1:
		errors.append("Email is required")
	if len(request.form["password"]) < 1:
		errors.append("Password is required")

	if len(errors) == 0:
		session["name"] = request.form["name"]
		session["email"] = request.form["email"]
		return redirect("/home")
	else:
		for error in errors:
			flash(error)
		return redirect("/")

@app.route("/test/<word>")
def something(word):
	if word == "purple":
		print "the word is purple"
	else:
		print "april o'neil"
	return render_template("test.html", color=word)

app.run(debug=True)