# file for SocketIO event handlers(e.g., connect, disconnect, message)
from flask_socketio import join_room, leave_room, send
from flask import session
from app import rooms, socketio

@socketio.on("connect")
def connect(auth):
    room_code = session.get("room")
    name = session.get("name")
    if not room_code or not name:
        send({"name": "System", "message": "Missing room or name in session."})
        return
    if room_code not in rooms:
        send({"name": "System", "message": "Room does not exist."})
        leave_room(room_code)
        return
    join_room(room_code)
    send({"name": name, "message": "joined the room!"}, to=room_code)
    rooms[room_code]["members"] += 1
    print(f"{name} joined room {room_code}")

@socketio.on("disconnect")
def disconnect():
    room_code = session.get("room")
    name = session.get("name")
    if not room_code or not name:
        send({"name": "System", "message": "Missing room or name in session."})
        return
    leave_room(room_code)
    if room_code in rooms:
        rooms[room_code]["members"] -= 1
        if rooms[room_code]["members"] <= 0:
            rooms.pop(room_code)
            send({"name": "System", "message": "Room has been deleted."})
        else:
            send({"name": name, "message": "left the room!"}, to=room_code)
            print(f"{name} left room {room_code}")

@socketio.on("message")
def message(data):
    room_code = session.get("room")
    name = session.get("name")
    if room_code not in rooms:
        send({"name": "System", "message": "Room does not exist."})
        return
    content = {
        "name": name,
        "message": data["data"]
    }
    send(content, to=room_code)
    rooms[room_code]["messages"].append(content)
    print(f"{name} said: {data['data']} in room {room_code}")
