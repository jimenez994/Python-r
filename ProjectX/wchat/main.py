from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = 'this_is_a_secret_ket'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message:' + msg)
    send(msg, broadcast= True)

if __name__ == '__main__':
    socketio.run(app)
 