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
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("home"))
    return render_template("room.html", code=room)

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "joined the room!"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    
    send({"name": name, "message": "left the room!"}, to=room)
    print(f"{name} left room {room}")

if __name__ == "__main__":
    socketio.run(app, debug=True)

# session is temporary storage for a user's session data that is stored on the server. The session can be manipulated by the server and we can change the value.
# if there is only one person in the room and we refresh the page, the room will be deleted.