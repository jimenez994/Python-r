from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "Real Madrid"
mysql = MySQLConnector(app, "the_wall")


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():

	errors = []

	if len(request.form['first']) < 1:
		errors.append("First name MUST be completed")
	elif len(request.form['first']) < 2:
		errors.append("First name MUST be longer than 1 letters.")
	
	if len(request.form['last']) < 1:
		errors.append("Last name MUST be completed")
	elif len(request.form['last']) < 2:
		errors.append("Last name MUST be longer than 1 letters.")

	if len(request.form['email']) < 1:
		errors.append("Email MUST be completed")
	elif not EMAIL_REGEX.match(request.form['email']):
		errors.append("Invalid email")
	
	if len(request.form['password']) < 1:
		errors.append("Password MUST be completed")
	elif len(request.form['password']) < 8: 
		errors.append("Password MUST be longer than 7 characters")
	
	if len(request.form['pass_confirm']) < 1:
		errors.append("Confirm password MUST be completed")
	elif request.form['pass_confirm'] != request.form['password']:
		errors.append("Password MUST match confirmed password")

	if errors == []:
		query = "INSERT INTO User (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :email, :password, NOW(), NOW())"
		data = {
			'first' : request.form['first'],
			'last' : request.form['last'],
			'email' : request.form['email'],
			'password' : bcrypt.hashpw(request.form['password'].encode(), bcrypt.gensalt())
		}
		user_id = mysql.query_db(query, data)
		session["user_id"] = user_id
		session["user_name"] = request.form['first']

		return redirect("/success")

	for error in errors:
		flash (error)

	return redirect("/")

@app.route('/login', methods=["POST"])
def login():
    errors = []
    if len(request.form['email']) < 1:
	    errors.append("Email MUST be completed")
    elif not EMAIL_REGEX.match(request.form['email']):
	    errors.append("Invalid email")
	
    if len(request.form['password']) < 1:
	    errors.append("Password MUST be completed")
    elif len(request.form['password']) < 8: 
	    errors.append("Password MUST be longer than 7 characters")
	
    query = "SELECT * FROM User WHERE email = '{}'".format(request.form['email'])
    resultSet = mysql.query_db(query)

    if len(resultSet) < 1:
	    errors.append("The email does not exist.")
    else:
        if bcrypt.checkpw(request.form['password'].encode(),resultSet[0]['password'].encode()): 
            session["user_id"] = resultSet[0]['id']
            print session["user_id"]
            session["user_name"] = resultSet[0]['first_name']
            return redirect("/success")
        else:
            errors.append("Password incorrect.")


	for error in errors:
		flash (error)	

	return redirect ('/')
@app.route("/post",methods=["POST"])
def post():
    print session["user_id"]
    if len(request.form["comment_field"]) < 10:
        return redirect("/success")
    else:
        data = {
            "content": request.form["comment_field"]
        }
        query = "INSERT INTO `the_wall`.`Post` (`content`, `created_at`, `updated_at`, `User_id`) VALUES (:content, NOW(), NOW(), {})".format(session["user_id"])
        mysql.query_db(query,data)
        return redirect("/success")
@app.route("/comment", methods=["POST"])
def comment():
    print session["user_id"]
    print len(request.form["comment"])
    print request.form["message_id"]
   
    query = "INSERT INTO Comment (content, created_at, updated_at, Post_id, User_id) VALUES (:content, NOW(), NOW(), :Post_id, :User_id)"
    data = {
            'content' : request.form['comment'],
            'Post_id' : request.form['message_id'],
            'User_id' : session['user_id']
    }
    mysql.query_db(query,data)
    #     print request.form["comment"]
    #     return redirect("/success")
    return redirect("/success")
@app.route("/success")
def success():
    if "user_id" not in session:
        flash("you have to login first")
        return redirect("/")

    messages = mysql.query_db("SELECT Post.content AS post, Post.id AS post_id, Post.created_at AS post_creates, User.first_name AS user FROM Post JOIN User ON User.id = Post.User_id ORDER BY Post.created_at desc")
    comments = mysql.query_db("SELECT Comment.content AS comment, Comment.created_at AS comment_time,Comment.User_id, User.first_name AS user, Post.id AS post_id FROM Comment JOIN Post ON Post.id = Comment.Post_id JOIN User ON User.id = Comment.User_id ORDER BY comment_time DESC")
        
    print comment
    return render_template("wall.html",messages=messages,comments=comments)

@app.route("/logout")
def logout():
	session.clear()
	return redirect("/")

app.run(debug=True)
