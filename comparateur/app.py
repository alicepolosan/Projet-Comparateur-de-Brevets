from flask import Flask, render_template, redirect, url_for
from form import BrevetForm
from flask_socketio import SocketIO
from calculs import calcul


app = Flask(__name__)
socketio = SocketIO(app)
app.config['SECRET_KEY'] = 'your secret key'


brevet_list = []
L = ['Albanie','Allemagne','Autriche','Bulgarie','Belgique','Chypre','Croatie','Danemark','Espagne','Estonie','Finlande','France','Grèce','Hongrie','Irlande','Islande','Italie','Lettonie','Liechtenstein (cf. Suisse)','Lituanie','Luxembourg','Macédoine du Nord','Malte','Monaco','Norvège','Pays-Bas','Pologne','Portugal','République Tchèque','Roumanie','Royaume-Uni','Saint-Marin','Serbie','Slovaquie','Slovénie','Suède','Suisse','Turquie']


@app.route('/', methods=('GET', 'POST'))
def index():
    form = BrevetForm()
    if form.validate_on_submit():
        if int(form.annee_delivrance.data) - 20 < int(form.annee_depot.data) and 0 < int(form.annee_depot.data) < int(form.annee_delivrance.data):
            cases_cochees = [form.p_0.data, form.p_1.data, form.p_2.data,form.p_3.data,form.p_4.data,form.p_5.data,form.p_6.data,form.p_7.data,form.p_8.data,form.p_9.data,form.p_10.data,form.p_11.data,form.p_12.data,form.p_13.data,form.p_14.data,form.p_15.data,form.p_16.data,form.p_17.data,form.p_18.data,form.p_19.data,form.p_20.data,form.p_21.data,form.p_22.data,form.p_23.data,form.p_24.data,form.p_25.data,form.p_26.data,form.p_27.data,form.p_28.data,form.p_29.data,form.p_30.data,form.p_31.data,form.p_32.data,form.p_33.data,form.p_34.data,form.p_35.data,form.p_36.data,form.p_37.data]
            pays = []
            for i in range(38):
                if cases_cochees[i] == 1:
                    pays.append(L[i])
            brevet_list.append({'annee_depot': form.annee_depot.data,
                                'annee_delivrance': form.annee_delivrance.data,
                                'pays': pays
                                })
            return redirect(url_for('resultats'))
        else:
            return render_template('erreur.html')
    return render_template('index.html', form=form)

@app.route('/resultats/')
def resultats():
    list0, list1, list2, list3, list4 = calcul(brevet_list)
    return render_template('resultats.html', brevet_list=brevet_list, list0 = list0, list1 = list1, list2 = list2, list3 = list3, list4 = list4)


if __name__=="__main__":
    socketio.run(app, port=5001)
