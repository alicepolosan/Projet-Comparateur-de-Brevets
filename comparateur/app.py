from flask import Flask, render_template 
from flask_socketio import SocketIO
#from backend import Calculs

app = Flask(__name__)
socketio = SocketIO(app)
#calculs = Calculs()

@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    socketio.run(app, port=5001)

