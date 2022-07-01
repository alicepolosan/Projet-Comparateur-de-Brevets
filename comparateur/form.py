from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField)
from wtforms.validators import InputRequired, Length

L = ['Albanie','Allemagne','Autriche','Bulgarie','Belgique','Chypre','Croatie','Danemark','Espagne','Estonie','Finlande','France','Grèce','Hongrie','Irlande','Islande','Italie','Lettonie','Liechtenstein (cf. Suisse)','Lituanie','Luxembourg','Macédoine du Nord','Malte','Monaco','Norvège','Pays-Bas','Pologne','Portugal','République Tchèque','Roumanie','Royaume-Uni','Saint-Marin','Serbie','Slovaquie','Slovénie','Suède','Suisse','Turquie']

class BrevetForm(FlaskForm):
    annee_depot = StringField('Annee de depot :', validators=[InputRequired(),
                                             Length(min=4, max=4)])
    annee_delivrance = StringField('Annee de delivrance :',
                                validators=[InputRequired(),
                                           Length(min = 4, max = 4)])
    #pays = []
    #for i in range (len(L)) : 
     #   pays.append(BooleanField(L[i]))

    p_0 = BooleanField(L[0])
    p_1 = BooleanField(L[1])
    p_2 = BooleanField(L[2])
    p_3 = BooleanField(L[3])
    p_4 = BooleanField(L[4])
    p_5 = BooleanField(L[5])
    p_6 = BooleanField(L[6])
    p_7 = BooleanField(L[7])
    p_8 = BooleanField(L[8])
    p_9 = BooleanField(L[9])
    p_10 = BooleanField(L[10])
    p_11= BooleanField(L[11])
    p_12= BooleanField(L[12])
    p_13= BooleanField(L[13])
    p_14= BooleanField(L[14])
    p_15= BooleanField(L[15])
    p_16= BooleanField(L[16])
    p_17= BooleanField(L[17])
    p_18= BooleanField(L[18])
    p_19= BooleanField(L[19])
    p_20= BooleanField(L[20])
    p_21= BooleanField(L[21])
    p_22= BooleanField(L[22])
    p_23= BooleanField(L[23])
    p_24= BooleanField(L[24])
    p_25= BooleanField(L[25])
    p_26= BooleanField(L[26])
    p_27= BooleanField(L[27])
    p_28= BooleanField(L[28])
    p_29= BooleanField(L[29])
    p_30= BooleanField(L[30])
    p_31= BooleanField(L[31])
    p_32= BooleanField(L[32])
    p_33= BooleanField(L[33])
    p_34= BooleanField(L[34])
    p_35= BooleanField(L[35])
    p_36= BooleanField(L[36])
    p_37= BooleanField(L[37])




    #for k in range(len(L)):
     #   globals()[f"p_{k}"] = BooleanField(L[k])
