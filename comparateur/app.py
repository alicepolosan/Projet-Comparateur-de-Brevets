from flask import Flask, render_template, redirect, url_for
from form import BrevetForm
from flask_socketio import SocketIO
from calculs import calcul


app = Flask(__name__)
socketio = SocketIO(app)
app.config['SECRET_KEY'] = 'your secret key'


brevet_list = [] # Liste qui contient les informations du remplissage du form (sous forme d'un dictionnaire). Les remplissages précédents sont gardés en mémoire ; brevetlist est donc une liste de dictionnaires).
L = ['Albanie','Allemagne','Autriche','Bulgarie','Belgique','Chypre','Croatie','Danemark','Espagne','Estonie','Finlande','France','Grèce','Hongrie','Irlande','Islande','Italie','Lettonie','Liechtenstein (cf. Suisse)','Lituanie','Luxembourg','Macédoine du Nord','Malte','Monaco','Norvège','Pays-Bas','Pologne','Portugal','République Tchèque','Roumanie','Royaume-Uni','Saint-Marin','Serbie','Slovaquie','Slovénie','Suède','Suisse','Turquie']


@app.route('/', methods=('GET', 'POST'))
def index():
    form = BrevetForm() # On instancie le formulaire. 
    if form.validate_on_submit(): # On vérifie que tous les validateurs demandés dans le fichiers form.py sont validés
        if int(form.annee_delivrance.data) - 20 < int(form.annee_depot.data) and 0 < int(form.annee_depot.data) < int(form.annee_delivrance.data): # On vérifie que la date de délivrance est bien moins de 20 ans après la date de dépot et que les deux dates sont bien positives
            # On met dans une liste un 1 si le pays a été coché et un 0 sinon.
            cases_cochees = [form.p_0.data, form.p_1.data, form.p_2.data,form.p_3.data,form.p_4.data,form.p_5.data,form.p_6.data,form.p_7.data,form.p_8.data,form.p_9.data,form.p_10.data,form.p_11.data,form.p_12.data,form.p_13.data,form.p_14.data,form.p_15.data,form.p_16.data,form.p_17.data,form.p_18.data,form.p_19.data,form.p_20.data,form.p_21.data,form.p_22.data,form.p_23.data,form.p_24.data,form.p_25.data,form.p_26.data,form.p_27.data,form.p_28.data,form.p_29.data,form.p_30.data,form.p_31.data,form.p_32.data,form.p_33.data,form.p_34.data,form.p_35.data,form.p_36.data,form.p_37.data]
            pays = [] # On va remplir une liste avec tous les pays qui ont été cochés.
            for i in range(38):
                if cases_cochees[i] == 1:
                    pays.append(L[i])
            brevet_list.append({'annee_depot': form.annee_depot.data,
                                'annee_delivrance': form.annee_delivrance.data,
                                'pays': pays
                                }) # On ajoute a brevetlist le dictionnaire contenant les réponses de l'utilisateur.
            return redirect(url_for('resultats')) # Si toutes les conditions sont satisafaites, on affiche le résultat.
        else:
            return render_template('erreur.html') # Si il y a un problème avec les dates, on renvoie cette erreur.
    return render_template('index.html', form=form) # Si le form n'est pas rempli, on reste sur la page du form.

@app.route('/resultats/')
def resultats():
    list0, list1, list2, list3, list4, cumulBE, cumulBU = calcul(brevet_list)
    ### socketio.emit("response", resultat)
    return render_template('resultats.html', brevet_list=brevet_list, list0 = list0, list1 = list1, list2 = list2, list3 = list3, list4 = list4, cumulBE = cumulBE, cumulBU = cumulBU)


if __name__=="__main__":
    socketio.run(app, port=5001)
