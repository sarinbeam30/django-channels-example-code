const WebSocket = require('ws');
const Window = require('window');
 
const window = new Window();

const socket = new WebSocket(
    'ws://'
    + '127.0.0.1:9000'
    + '/ws/location'
    + '/'
);

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log("DATA : " + e.data + '\n');
}

socket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};