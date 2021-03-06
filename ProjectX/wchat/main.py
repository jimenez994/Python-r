from flask import Flask, session, redirect, render_template, request, flash, url_for, json
from flask_socketio import SocketIO, emit, join_room
from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from functools import wraps
from PIL import Image
from datetime import datetime
import base64
import os
import uuid
import io
from mysqlconnection import MySQLConnector

import bcrypt

MugShot_PATH = 'static/mugshot'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
MugShot_FOLDER = os.path.join(APP_ROOT, MugShot_PATH)

app = Flask(__name__)
app.secret_key = 'super secret string'  # Change this!
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message = "Please LOG IN"
login_manager.login_message_category = "info"

socketio = SocketIO(app)
async_mode = "eventlet"
mysql = MySQLConnector(app, "zchat")

class User(UserMixin):
    pass

def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        get_fun = func(*args, **kwargs)
        return json.dumps(get_fun)

    return wrapper


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

@app.route('/')
@app.route('/index', methods=['GET'])
@login_required
def index():
    user_id = session.get('user_id')
    messages = mysql.query_db(
        "SELECT History.message AS message, History.created_at AS created_time FROM History")
    
    print user_id
    print "***********$$$$$$$$$$"
    print request.cookies.get('user_id')
    print "***********$$$$$$$$$$"
    return render_template('/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user_id = session.get('user_id')

    if request.method == 'GET':
        return render_template("login.html")

    if current_user.is_authenticated and query_user(user_id):
        return redirect(url_for('index'))

    query = "SELECT * FROM User WHERE username = '{}'".format(
        request.form['username'])
    resultSet = mysql.query_db(query)
    if len(resultSet) < 1:
        return redirect("/login")
    if bcrypt.checkpw(request.form['password'].encode(), resultSet[0]['password'].encode()):
        user = User()
        user.id = request.form['username']
        login_user(user, remember=True)
        flash('Logged in successfully')
        
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    query = "INSERT INTO User (username, password, img, created_at, updated_at) VALUES (:username, :password, :img, NOW(), NOW())"
    data = {
        'username': request.form['username'],
        'password': bcrypt.hashpw(request.form['password'].encode(), bcrypt.gensalt()),
        'img': 'default.png'
    }
    mysql.query_db(query, data)
    return redirect(url_for("index"))

@app.route('/API_check_UserNameExist', methods=['POST'])
@to_json
def api_check_user_name_exist():
    username = request.json['username']
    user = UserAccounts.query.filter_by(UserName=username).first()
    if not user:
        return "not_exist"
    return "exist"


@socketio.on('join')
def join(message):
    join_room(message['room'])
    print('join')

@socketio.on('connect')
def test_connect():
    emit('connected', session.get('user_id'))
    Userid = session.get('user_id')
    print(Userid, 'connectd')


@socketio.on('sendInquiry')
def send_inquiry(msg):
    user_id = session.get('user_id')
    print '*************************!'
    # still getting None
    print session.get('user_id')
    print '*************************!'
    # need some work on user in session 
    user_id = session.get('user_id')
    create_date = datetime.now()
    # 
    query = "INSERT INTO History (message, created_at, updated_at, User_id) VALUES (:message, NOW(), NOW(), :User_id)"
    data_message = {
        'message': msg,
        'User_id': 1,
    }
    mysql.query_db(query, data_message)
    # 
    user = mysql.query_db(
        "SELECT * FROM User WHERE id = '{}'".format(1))
    data = {
        'time': create_date.strftime('%H:%M'),
        'Name': user_id,
        'PictureUrl': user[0]['img'],
        'msg': msg
    }
    emit('getInquiry', data, room=msg['room'])

if __name__ == '__main__':
    socketio.run(app)
 
app.run(debug=True)
