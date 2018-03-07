from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bla'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('message')
def handleMessage(msg):
    print('message'+ msg)
    send(msg, broadcast=True)

if __name__ == '__main_':
    socketio.run(app)