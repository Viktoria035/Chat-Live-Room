# file for Flask route functions(in this case -> the home and room routes)
from flask import Blueprint, render_template, request, session, redirect, url_for
from app import rooms
from .utils import generate_unique_code
from flask import current_app as app

home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/", methods=["GET", "POST"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join")
        create = request.form.get("create")

        if join and not code:
            return render_template("home.html", error="Code is required when you want to join a room!", name=name)
        elif join and code not in rooms:
            return render_template("home.html", error="Room does not exist!", code=code, name=name)
        
        room_code = code
        if create:
            room_code = generate_unique_code()
            rooms[room_code] = {"members": 0, "messages":[]}

        session["name"] = name
        session["room"] = room_code
        return redirect(url_for("home.room"))
        
    return render_template("home.html")

@home_blueprint.route("/room")
def room():
    room_code = session.get("room")
    name = session.get("name")
    if not room_code or not name or room_code not in rooms:
        return redirect(url_for("home.home"))
    return render_template("room.html", code=room_code, messages=rooms[room_code]["messages"])
