from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, SocketIO, send
import random
from string import ascii_uppercase

# initialize the flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = 'fksdhkdshfd'
socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app, debug=True)