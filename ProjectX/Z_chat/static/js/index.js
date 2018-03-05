$(function () {
    

    var socket = io.connect('http://127.0.0.1:5000');
    socket.on('connect', function () {
        socket.emit('join', {room: 'A_Room'})
        console.log('User has connected!')
    })

});