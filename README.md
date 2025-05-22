## Overview

**Chat Live Room** is a real-time chat application that enables multiple users to create or join chat rooms and communicate instantly. It is built with Python using Flask and Flask-SocketIO for real-time, bi-directional communication via WebSockets.

The project was inspired by various YouTube tutorials and serves as a personal learning exercise to gain hands-on experience with Flask and WebSocket integration.

The current interface is intentionally simple, focusing on core chat functionality. Authentication and authorization are not included at this stage, but could be valuable future improvements.


---


## Features

- 🔐 **Room Code System** – Users can create a private chat room with a unique 4-letter code or join an existing one.
- 💬 **Real-Time Messaging** – Built using Flask-SocketIO for instant, bi-directional communication.
- 🖥️ **Responsive UI** – Clean and centered interface with intuitive layout using HTML & CSS.
- 🧠 **Session Management** – Tracks user name and room code across the session.
- 🔌 **Socket.IO Events** – Handles user connections, disconnections, and messages efficiently.
- ♻️ **Automatic Room Cleanup** – Deletes a room when all users leave.


---


## Tech Stack

- **Backend**: Python, Flask, Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript
- **WebSockets**: Socket.IO
- **Templating**: Jinja2
- **Session Management**: Flask's built-in session system


---


## Project Structure

```
chat-live-room/
├── app/ # Main application package
│ ├── init.py # Flask app factory and SocketIO init
│ ├── routes.py # Blueprint routes for home and chat 
| ├── socketio_events.py # SocketIO event handlers
│ ├── utils.py # Utility function to generate room 
├── static/
│ ├── css/style.css # Stylesheets
│ ├── js/chat.js
│ └── images/... # Any static images
├── templates/
│ ├── base.html # Base template
│ ├── home.html # Home page
│ └── room.html # Room page
├── main.py # Entry point to run the server
├── requirements.txt # Python dependencies
└── README.md # This file
```


---


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Viktoria035/Chat-Live-Room.git
    cd Chat-Live-Room
    ```
2. Create and activate a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Linux/macOS
    ./venv/Scripts/activate.bat # On Windows(if you are using Command Prompt)
    ./venv/Scripts/Activate.ps1 # On Windows(if you are using PowerShell)
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the server
    ```bash
    python main.py
    ```
5. Open in your browser


---


## Future improvements

1. Authentication System
2. User list per room
3. History of chats
