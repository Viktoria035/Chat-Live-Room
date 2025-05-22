from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()
rooms = {}

def create_app():
    # Initialize the Flask application
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    # put the secret key here; this is just a random string
    # in a real application, you should use a more secure method to generate and store the secret key
    app.config["SECRET_KEY"] = 'fksdhkdshfd'

    # Register Blueprints
    from .routes import home_blueprint
    app.register_blueprint(home_blueprint)

    # Attach shared objects
    app.rooms = rooms
    
    # Initialize SocketIO
    socketio.init_app(app)

    from . import socketio_events

    return app
