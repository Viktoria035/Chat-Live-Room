var socketio = io();

const messages = document.getElementById('messages');

const createMessage = (name, msg) => {
    const content = `
        <div class="user-message">
            <span>
                <strong>${name}</strong>: ${msg}
            </span>
            <span class="muted">
                ${new Date().toLocaleString()}
            </span>
        </div>
    `;
    messages.innerHTML += content;
};

socketio.on('message', (data) => {
    createMessage(data.name, data.message);
});

const sendMessage = () => {
    const message = document.getElementById('message');
    if (!message.value) {
        alert('Please enter a message');
        return;
    }
    socketio.emit('message', { data: message.value });
    message.value = '';
};
