from flask import Flask, session, redirect, url_for, render_template, request
from flask_socketio import emit, join_room, leave_room, SocketIO
from flask import session

app = Flask(__name__)
app.secret_key = 'super secret string'
socketio = SocketIO(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.form['username'] and request.form['room'] != '':
        # storing user and room in session
        session['name'] = request.form['username']
        session['room'] = request.form['room']
        return redirect(url_for('.chat'))
    return render_template('index.html')

@app.route('/chat')
def chat():
    name = session.get('name','')
    room = session.get('room','')
    print name
    print room
    if name == '' or room == '':
        return redirect('/')
    return render_template('chat.html', name=name, room=room)

@app.route('/logout')
def logout():
    # clears the session
    session.clear()
    return render_template('index.html')

# notifies when someone join the room 
@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has join'}, room=room)

# sending messages
@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    emit('message', {'msg': session.get('name')+ ':'+ message['msg']}, room=room)

# notifies when a user leaves the room
@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status',{'msg':session.get('name') + 'has left'}, room=room)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")
