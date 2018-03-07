from flask_socketio import emit, join_room, leave_room
from flask import session


if __name__ == '__main__':
    socketio.run(app)
