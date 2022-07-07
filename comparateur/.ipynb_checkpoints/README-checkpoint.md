## Prérequis pour l'exécution du programme :

Liste des modules et packages à installer pour faire fonctionner le comparateur ainsi que leurs versions :

- flask (2.1.2)
- flask-socketio (5.2.0)
- flask-wtf (1.0.1)
- jinja2, fonctionne avec JavaScript (2.1.2)
- numpy (1.24.2)
- pandas (1.4.2)
- wtforms, fonctionne avec JavaScript (3.0.1)

On installe le tout (flask, flask-socketio, flask-wtf, numpy et pandas) avec un pip install.

- Version de pip utilisée : 21.2.4 
- Version de python utilisée : 3.9.12.


## Exécution du programme : 

Lancer un terminal à la racine du fichier comparateur et exécuter la ligne : 
```python
python app.py
```

Dans un navigateur (firefox de préférence), saisir : `localhost:5001`. La page suivante s'ouvre :

![](média/démo.png)

<!-- #region app.py ``` -->
## Fonctionnement de l'interface

Vous pouvez alors saisir les informations du brevet que vous voulez estimer :

- l'année de dépôt du Brevet
- l'année de délivrance
- les pays dans lesquelles vous voulez que votre invention soit protégée.

Une fois les informations saisies, cliquez sur le bouton 'valider'.
Les résultats s'affichent alors sur un graphique sur lequel vous pouvez lire : 

- sur les barres : les coûts par année pour le brevet unitaire et le brevet européen, depuis la date de validation jusqu'à la date de dépôt + 20 ans.
- sur les courbes : les coûts cumulés pour le brevet unitaire et le brevet européen.
<!-- #endregion -->
