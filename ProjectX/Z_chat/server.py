from flask import Flask, session, redirect, render_template, request, flash , url_for
from flask_socketio import SocketIO, emit, join_room
from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from mysqlconnection import MySQLConnector
import os
import bcrypt

MugShot_PATH = 'static/mugshot'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
MugShot_FOLDER = os.path.join(APP_ROOT, MugShot_PATH)

app = Flask(__name__)
app.secret_key = 'REAL MADRID'
mysql = MySQLConnector(app, "zchat")
login_manager = LoginManager()
login_manager.init_app(app)

socketio = SocketIO(app)
async_mode = "eventlet"

class User(UserMixin):
    pass

def query_user(username):
    query = "SELECT * FROM User WHERE username = '{}'".format(username)
    resultSet = mysql.query_db(query)
    if len(resultSet) < 1:
        return False
    return True

@login_manager.user_loader
def user_loader(username):
    if query_user(username):
        user = User()
        user.id = username
        return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    user_id = session.get('user_id')

    if request.method == 'GET':
        return render_template("login.html")
    
    query = "SELECT * FROM User WHERE username = '{}'".format(request.form['username']) 
    resultSet = mysql.query_db(query)
    if len(resultSet) < 1:
        return redirect("/login")
    if bcrypt.checkpw(request.form['password'].encode(), resultSet[0]['password'].encode()):
        user = User()
        user.id = request.form['username']
        login_user(user, remember=True)
        flash('Logged in successfully')
        return redirect(url_for('index'))
    return redirect("/login")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    query = "INSERT INTO User (username, password, img, created_at, updated_at) VALUES (:username, :password, :img, NOW(), NOW())"
    data = {
        'username': request.form['username'],
        'password': bcrypt.hashpw(request.form['password'].encode(), bcrypt.gensalt()),
        'img':'default.png'
    }
    mysql.query_db(query, data)
    return redirect(url_for("index"))


@app.route('/index')
def index():
    user_id = session.get('user_id')
    print user_id
    return render_template("index.html", **locals())

@app.route('/logout')
def logout():
    print session.get('user_id')
    logout_user()
    print session.get('user_id')
    return redirect(url_for('login'))
app.run(debug=True)

@socketio.on('join')
def join(message):
    join_room(message['room'])
    print('join')

@socketio.on('connect')
def test_connect():
    print('connect')

@socketio.on('sendInquiry')
def send_inquiry(msg):
    user_id = session.get('user_id')
    if msg['msg'] != '':
        query = "INSERT INTO History (message, created _at, updated_at, User_id) VALUES (:message, NOW(), NOW(), :User_id)"
        data_message = {
            'message': msg['msg'],
            'User_id': user_id,
        }
        mysql.query_db(query, data_message)
    user = mysql.query_db("SELECT * FROM User WHERE username = '{}'".format(user_id))
    data = {
        'time': user[0]['created_at'],
        'Name': user_id,
        'PictureUrl': user[0]['img'],
        'msg': msg['msg']
    }
    emit('getInquiry', data, room=msg['room'])

