from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("send_message")
def handle_send_message(data):
    # send to ALL except sender
    emit("receive_message", data, broadcast=True, include_self=False)

if __name__ == '__main__':
    port= int(os.environ.get("PORT",10000))
    socketio.run(app, host="0.0.0.0",port=port)
