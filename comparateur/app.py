from flask import Flask, render_template, redirect, url_for
from form import BrevetForm
from flask_socketio import SocketIO
from calculs import calcul


app = Flask(__name__)
socketio = SocketIO(app)
app.config['SECRET_KEY'] = 'your secret key'


brevet_list = []


@app.route('/', methods=('GET', 'POST'))
def index():
    form = BrevetForm()
    if form.validate_on_submit():
        brevet_list.append({'annee_depot': form.annee_depot.data,
                             'annee_delivrance': form.annee_delivrance.data,
                             'pays': form.pays.data,
                             })
        return redirect(url_for('resultats'))
    return render_template('index.html', form=form)

@app.route('/resultats/')
def resultats():
    resultat = calcul(brevet_list)
    return render_template('resultats.html', brevet_list=brevet_list, resultat = resultat)


if __name__=="__main__":
    socketio.run(app, port=5001)