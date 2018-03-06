from flask import Flask, render_template, redirect, request, flash, session
from flask_socketio import SocketIO, send
from mysqlconnection import MySQLConnector
import re
import bcrypt

app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_secret"
mysql = MySQLConnector(app, "chatchat")
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
    print "i got here"
    errors = []
    if len(request.form['username']) < 1:
        errors.append("Must have a username")
    elif len(request.form['username']) < 5:
        errors.append("Username must be longer")
    print "i got here 1"

    query = "SELECT * FROM User WHERE username = '{}'".format(request.form['username'])
    resultSet = mysql.query_db(query)
    print "i got here 2"

    if len(resultSet) > 0:
        errors.append("The username already exists")
    if len(request.form["password"]) < 1:
        errors.append("Password MUST be completed")
    elif len(request.form["password"]) < 8:
        errors.append("Password MUST be at least 8 characters")
    print "i got here 3"

    if errors == []:
        print "i got here 3.5"
        query = "INSERT INTO User (username, password, created_at, updated_at) VALUES (:username, :password, NOW(), NOW())"
        data = {
            "username" : request.form['username'],
            "password": bcrypt.hashpw(request.form['password'].encode(), bcrypt.gensalt())
        }
        print "iddddddddddddddddddddddddd"
        user_id = mysql.query_db(query, data)
        print user_id
        session["user_id"] = user_id
        print "bla 2"
        session["user_name"] = request.form['username']
        print "i got here 4"

        return redirect("/dashboard")
    for error in errors:
        flash (error)
    return redirect("/")
@app.route('/login', methods=["POST"])
def login():
    errors = []
    if len(request.form['username']) < 1:
        errors.append("missing username")
    if len(request.form["password"]) < 1:
        errors.append("missing password")
    elif len(request.form["password"]) < 8:
        errors.append("Password MUST be at least 8 characters")
    
    query = "SELECT * FROM User WHERE username = '{}'".format(request.form['username'])
    resultSet = mysql.query_db(query)

    if len(resultSet) < 1:
        errors.append("the username does not exists")
    else:
        if bcrypt.checkpw(request.form["password"].encode(), resultSet[0]['password'].encode()):
            session['user_id'] = resultSet[0]['id']
            return redirect("/dashboard")
        else: 
            errors.append('password is incorrect')
    for error in errors:
        flash (error)
    return redirect ("/")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("you have to be login first")
        return redirect("/")
    user_id = session["user_id"] 
    messages = mysql.query_db("SELECT History.message AS message, History.created_at AS created_at FROM History")
    return render_template('dashboard.html', messages= messages, user_id = user_id)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@socketio.on('message')
def handleMessage(msg):
    print session.get("user_id")
    user_id = 1
    query = "INSERT INTO History (message, created_at, updated_at, User_id) VALUES (:message, NOW() , NOW(),:User_id)"
    data = {
        'message': msg,
        'User_id': user_id
    }
    mysql.query_db(query, data)
    send(msg, broadcast =True)

app.run(debug=True)

