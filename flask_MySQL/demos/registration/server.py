from flask import Flask, session, render_template, redirect, flash, request
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = "I can't believe this key is so secret"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9!@#\$%^&*]{8,}$')

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	errors = []

	# check email
	if len(request.form["email"]) < 1:
		errors.append("Email cannot be blank")
	elif not EMAIL_REGEX.match(request.form["email"]):
		errors.append("Invalid email")

	# check first name
	if len(request.form["first"]) < 1:
		errors.append("First name cannot be blank")
	elif not request.form["first"].isalpha():
		errors.append("First name must contain only letters") 

	# check last name
	if len(request.form["last"]) < 1:
		errors.append("Last name cannot be blank")
	elif not request.form["last"].isalpha():
		errors.append("Last name must contain only letters")

	# password
	if len(request.form["password"]) < 1:
		errors.append("Password cannot be blank")
	elif len(request.form["password"]) < 8:
		errors.append("Password must be 8 characters or more")

	# confirm password
	if len(request.form["confirm"]) < 1:
		errors.append("Confirm Password cannot be blank")
	elif request.form["password"] != request.form["confirm"]:
		errors.append("Confirm Password must match Password")

	# date of birth validations
	if len(request.form["dob"]) < 1:
		errors.append("Date of Birth is required")
	else:
		day = datetime.strptime(request.form["dob"], "%Y-%m-%d")
		today = datetime.now()
		if day > today:
			errors.append("Date of Birth must be in the past")

	# something check
	if 'something' not in request.form:
		errors.append("You need to select something")

	for error in errors:
		flash(error)

	return redirect("/")

app.run(debug=True)