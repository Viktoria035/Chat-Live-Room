from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, SocketIO, send
import random
from string import ascii_uppercase

# initialize the flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = 'fksdhkdshfd'
socketio = SocketIO(app)

rooms = {}

def generate_unique_code(length):
    while True:
        code = "".join(random.choices(ascii_uppercase, k=length))
        if code not in rooms:
            return code

# create route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False) # False is default value
        create = request.form.get("create", False)

        if not name:
            return render_template("home.html", error="Name is required!", code=code, name=name)
        
        if join != False and not code:
            return render_template("home.html", error="Code is required!", code=code, name=name)
        
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages":[]}
        elif code not in rooms:
            return render_template("home.html", error="Room does not exist!", code=code, name=name)
        
        session["name"] = name
        session["room"] = room
        return redirect(url_for("room"))
        
    return render_template("home.html")

@app.route("/room")
def room():
    return render_template("room.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)

# session is temporary storage for a user's session data that is stored on the server. The session can be manipulated by the server and we can change the value.