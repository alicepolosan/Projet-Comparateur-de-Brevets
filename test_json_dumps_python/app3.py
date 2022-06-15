from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO
from calculs3 import calcul


app = Flask(__name__)
socketio = SocketIO(app)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/', methods=('GET', 'POST'))
def resultats():
    resultat = calcul([])
    socketio.emit("response", resultat)
    return render_template('index3.html', resultat = resultat)


if __name__=="__main__":
    socketio.run(app, port=5001)