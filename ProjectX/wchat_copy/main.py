from flask import Flask, render_template
from flask_socketio import SocketIO, send
from mysqlconnection import MySQLConnector



app = Flask(__name__)
app.config["SECRET_KEY"] = 'this_is_a_secret_ket'
mysql = MySQLConnector(app, "wchat")

socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message:' + msg)

    query = "INSERT INTO History (message, created_at, updated_at) VALUES (:message, NOW(), NOW())"
    data = {
        'message': msg,
    } 
    mysql.query_db(query, data)
    send(msg, broadcast= True)

@app.route('/')
def index():
    messages = mysql.query_db("SELECT History.message AS message, History.created_at AS created_time FROM History")

    return render_template('index.html', messages= messages)

if __name__ == '__main__':
    socketio.run(app)
 
