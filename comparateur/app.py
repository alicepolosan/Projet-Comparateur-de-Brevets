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
    list0, list1, list2, list3, list4 = calcul(brevet_list)
    ### socketio.emit("response", resultat)
    return render_template('resultats.html', brevet_list=brevet_list, list0 = list0, list1 = list1, list2 = list2, list3 = list3, list4 = list4)


if __name__=="__main__":
    socketio.run(app, port=5001)