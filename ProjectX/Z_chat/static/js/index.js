$(function () {

    var socket = io.connect('http://127.0.0.1:5000');
    
    socket.on('connect', function () {
        socket.emit('join', {room: 'A_Room'})
        console.log('User has connected!')
    })
    function newMessage() {
        var msg = $('.message-input').val();
        if ($.trim(msg) ==''){
            return false;
        }
        var obj = {
            msg: msg,
            room: 'A_Room'
        };
        socket.emit('sendInquiry', obj);
    }
    $('.message-submit').click(function () {
        newMessage();
    })
});