import pandas as pd
import numpy as np
import json 

#On  crée manuellement une dataframe pandas qui reprend les données du fichier excel fourni par les porteurs de projet
#On commence par définir la liste complète des pays concernés 
Pays = ['Albanie', 'Allemagne', 'Autriche', 'Bulgarie', 'Belgique', 'Chypre', 'Croatie', 'Danemark', 'Espagne', 'Estonie', 'Finlande', 
        'France','Grèce', 'Hongrie', 'Irlande', 'Islande', 'Italie', 'Lettonie', 'Liechtenstein (cf. Suisse)', 'Lituanie', 'Luxembourg', 'Macédoine du Nord', 
        'Malte', 'Monaco', 'Norvège', 'Pays-Bas', 'Pologne', 'Portugal', 'République Tchèque', 'Roumanie', 'Royaume-Uni', 'Saint-Marin', 
        'Serbie', 'Slovaquie', 'Slovénie', 'Suède', 'Suisse', 'Turquie']
n=len(Pays)

#On définit ensuite la colonne de la dataframe indiquznt, pour chaque pays, s'il fait partie de la convention du brevet unitaire
BU= ['non']*n

L_oui=[1,2,3,4,7,9,10,11,16,17,19,20,22,25,27,34,35]
for i in L_oui:
    BU[i]= 'oui'

#On crée ensuite les 20 colonnes donnant, pour chaque pays et pour chaque année, les anuités à payer au cours de l'année en question
indice= Pays.index('République Tchèque')

#Annuités de l'année 1 
année_1=[0]*n
année_1[indice]= 41.00   #Au cours de l'année 1, seule la République Chèque fait payer une annuité

#Annuités de l'année 2
année_2=[0]*n
année_2[0]=42
année_2[1]=42
année_2[11]=38
année_2[13]=46.55
année_2[23]=30
année_2[indice]=41

#Les listes d'annuités des années suivantes sont reprises directement du fichier Excel, en assignant, pour chaque année, la valeur de 0 aux annuités des pays qui n'en font pas payer  
année_3=[50,70,0,20,40,50,35,0,18.48,64,200,38,20,46.55,60,84,0,90,0,81,33,13,34.94,50,0,0,0,0,41,150,0,0,95,66,0,135,0,35]

année_4=[67,70,0,20,55,60,42,148,23.06,77,125,38,50,233,90,97,0,120,105.26,92,41,16,46.59,55,134,40,53.15,0,41,160,0,70,115,
         82.50,34,144,105.26,41]

année_5=[83,90,0,72,75,80,58,168,44.11,96,150,38,80,290,114,106,60,140,126.32,115,52,20,58.23,90,168,100,64,51.56,82,
         180,87.5,70,135,99.5,42,164,126.32,61]

année_6=[100,130,104,92,95,100,75,188,65.10,120,200,76,90,393,134,115,90,160,147.37,139,66,23,69.88,125,203,160,74,77.34,
         82,200,112.50,70,160,116,50,183,147.37,69]

année_7=[117,180,208,113,110,120,85,215,107.47,135,250,96,100,393,150,128,120,180,168.42,162,82,26,81.53,140,223,220,85,103.13,
         82,220,137.50,70,190,132.50,60,202,168.42,77]

année_8=[150,240,313,138,135,140,110,242,133.78,155,300,136,115,393,176,141,170,220,189.47,185,99,30,93.17,145,259,280,96,
         154.69,82,240,162.50,140,215,149,70,231,189.47,86.47]

année_9=[167,290,417,195,165,160,125,275,167.88,180,350,180,140,393,194,158,200,270,231.58,208,115,33,104.82,155,289,340,117,
         309.38,122,260,187.5,140,240,165.5,80,260,231.58,94]

année_10=[208,350,522,256,185,180,160,309,216.06,205,400,220,190,393,220,176,230,320,273.68,231,131,50,116.47,175,325,400,138,
          360.95,163,280,212.50,140,270,199,110,289,273.68,103]

année_11=[225,470,626,307,215,200,200,342,270.82,245,450,260,240,393,242,193,310,320,315.79,289,148,65,128.12,220,355,500,
          159,360.95,245,300,237.5,140,325,232,154,327,315.79,117]

année_12=[250,620,731,359,240,240,240,376,317.98,285,500,300,300,393,265,210,410,320,357.89,289,165,80,139.60,255,391,600,170,
          412.51,326,320,275,270,380,265.50,200,366,357.89,136]

année_13=[292,760,835,410,275,280,280,410,365.05,320,550,350,400,407,285,232,530,320,421.05,289,180,97,141.41,290,426,700,191,
          464.07,407,340,325,270,430,298.50,234,404,421.05,157]

année_14=[333,910,940,461,320,320,306,443,412.56,360,600,400,500,407,311,262,600,320,484.21,289,198,113,163.06,335,457,800,202,
          515.64,489,370,375,270,485,331.50,274,443,484.21,178]

année_15=[375,1060,1044,512,360,360,346,483,440.59,405,650,460,600,407,335,294,650,320,547.37,289,213,130,174.10,350,492,900,
          223,567.19,571,400,450,270,540,365,310,481,547.37,205.60]

année_16=[417,1230,1148,563,400,420,400,524,458.85,450,700,520,700,407,356,324,650,420,631.58,347,230,145,186.35,365,528,1000,
          244,567.19,652,500,525,400,595,398,390,520,631.58,225]

année_17=[458,1410,1253,615,450,480,466,564,490,495,750,580,800,422,382,364,650,420,715.79,347,246,160,198,375,558,1100,266,
          670.33,734,500,587.50,460,645,464.50,510,558,715.79,250]

année_18=[500,1590,1357,666,500,540,613,604,490,540,800,650,900,422,408,400,650,420,800,347,262,177,209.64,380,588,1200,287,
          670.33,815,500,650,530,700,531,654,597,800,267]

année_19=[542,1760,1566,768,555,600,773,645,490,585,850,730,1000,436,438,438,650,420,905.26,347,281,193,221.29,400,629,1300,
          308,721.89,897,500,712.50,600,755,597,870,635,905.26,282]

année_20=[583,1940,1775,871,600,660,920,685,490,630,900,800,1100,436,468,483,650,420,1010.53,347,300,210,232.94,430,660,1400,
          330,721.89,978,500,762.50,650,810,663.50,1100,674,1010.53,294]

# Ceci est la liste des coûts associés au brevet unitaire (BU) : la liste est de taille 21, le 1er coefficient correspondant au coût de demande d'effet unitaire
couts_BU_annees=[1000,0,0,0,1000,355,515,670,845,1030,1205,1500,1805,2145,2495,2870,3280,3680,4095,4495,4895]

#On crée alors le dictionnaire des colonnes de la dataframe: 
# La 1re colonne est celle qui renseigne sur l'appartenance des pays au BU
# La 2è colonne est celle des coûts de validation nationale pour l'ensemble des pays dans le cas du brevet européen (BE) 
# La dataframe comprend seulement les coûts de validation nationale et des annuités à payer au cours des 20 ans, dans le cadre du BE --> les informations
#relatives au BU sont contenues dans la liste couts_BU_annees ci-dessus, qui ne fait pas partie de la dataframe
cols_dict={"BU": BU,
"validation nationale/demande d'effet unitaire":[5000, 250,5000,5000, 250, 5000, 3500, 3500, 3500, 5000, 3500, 200, 
                                                            5000, 3500, 250, 3500, 5000, 3500, 200, 5000, 200, 3500, 5000, 200, 
                                                            3500, 3500, 5000, 5000, 5000, 5000, 250, 5000, 5000, 5000, 3500, 
                                                            3500, 200, 5000],
          "année 1": année_1,
          "année 2": année_2,
          "année 3": année_3,
          "année 4":année_4,
          "année 5":année_5,
          "année 6":année_6,
          "année 7": année_7,
          "année 8": année_8,
          "année 9": année_9,
          "année 10": année_10,
          "année 11": année_11,
          "année 12": année_12,
          "année 13": année_13,
          "année 14": année_14,
          "année 15": année_15,
          "année 16": année_16,
          "année 17": année_17,
          "année 18": année_18,
          "année 19": année_19,
          "année 20": année_20,
          }
#Création de la dataframe, indexée par les pays
df = pd.DataFrame(cols_dict, index = Pays)

#Ci-dessous sont implémentées 5 fonctions de calculs:

#La fonction liste_annees renvoie la liste des années au cours duquel le brevet est effectif, donc à partir de la date de délivrance
#jusqu'à la date de fin, c'est-à-dire 20 ans après la date de dépôt. En effet, seules ces années sont prises en compte dans le calcul
# des coûts, car aucune annuité n'est payée avant l'année de délivrance.

def liste_annees (brevet_list): #brevet_list est un dictionnaire de listes, chaque liste comportant 3 éléments:
    # l'année de dépôt, l'année de délivrance, et la liste des pays souhaités
    dic=brevet_list[-1] #on récupère la dernière liste 
    annee_depot=int(dic['annee_depot'])
    annee_delivrance=int(dic['annee_delivrance'])
    annee_fin= annee_depot + 20
    year_list= list(np.arange(annee_delivrance,annee_fin))
    return year_list

#La fonction couts_annees renvoie prend en argument, les informations d'année de dépôt, d'année de délivrance et la liste des pays
# où il est souhaité que le brevet entre en vigeur, et renvoie en sortie deux listes : la liste des coûts à payer par année avec le BE classique
# et la liste des coûts annuels si on choisit d'adopter le BU. 
def couts_année (brevet_list):
    n=len(liste_annees(brevet_list))   
    dic=brevet_list[-1]
    pays= dic['pays'] #liste des pays recherchés
    data= df.loc[pays]  #dataframe des coûts pour ces pays
    indices=["validation nationale/demande d'effet unitaire"]+ (list(data.columns))[23-n:] # seules les années à partir de l'année de délivrance nous intéressent car 
    #les coûts ne sont payés qu'après l'année de délivrance. Il faut donc extraire les colonnes de la datframe qui correspondent à ces années-là
    data=data[indices] #data est la dataframe sur laquelle nous faisons le calcul des coûts annuels: les lignes correspondent aux pays voulus et aux coûts associés, et les colonnes à l'une des années de validité du brevet accompagnées de la colonne des coûts de validation par pays
    sommes= data.sum() #pour chaque année,on somme les annuités des pays
    couts_BE= json.dumps((sommes.to_numpy().tolist()))  
    couts_BU_provisoire=[couts_BU_annees[0]] + couts_BU_annees [22-n:]
    for country in pays: #en choisissant le BU, il faut ajouter les coûts à payer pour les pays souhaités qui ne sont pas intégrés au BU
        if df.loc[country,'BU']=='non': # on vérifie si le pays n'est pas dans le BU
           couts_BU_provisoire = (np.array(couts_BU_provisoire) + (data.loc[country]).to_numpy()).tolist() # on actualise la liste des coûts en lui ajoutant les coûts annuels associés à ce pays 
    couts_BU = json.dumps(couts_BU_provisoire)  
    return couts_BE, couts_BU


def couts_cumulés (brevet_list):
    n=len(liste_annees(brevet_list))
    dic=brevet_list[-1]
    pays= dic['pays']
    data= df.loc[pays]
    indices=["validation nationale/demande d'effet unitaire"]+ (list(data.columns))[23-n:] 
    data=data[indices]
    sommes= data.sum()
    couts_BE=(np.cumsum(sommes.to_numpy()).tolist())  #on renvoie cette fois-ci, non pas les listes des coûts annuels obtenus avec l'ensemble des pays recherchés,
#mais les coûts cumulés sur les années     
    last_cumul_BE=couts_BE[-1] #on récupère le coût total en choisissant le BE
    couts_BE=json.dumps(couts_BE)
    couts_BU= np.cumsum(np.array([couts_BU_annees[0]] + couts_BU_annees [22-n:]))
    for country in pays:
        if df.loc[country,'BU']=='non':
           couts_BU = couts_BU + np.cumsum((data.loc[country]).to_numpy())
    couts_BU = couts_BU.tolist()     
    last_cumul_BU=couts_BU[-1] # on récupère le coût total à payer en choisissant le BU
    couts_BU=json.dumps(couts_BU) 
    return couts_BE, couts_BU, np.int(last_cumul_BE),np.int(last_cumul_BU)

#La fonction calcul permet d'agréger les résultats renvoyés par les 3 fonctions précédentes
def calcul (brevet_list):
    couts_BE_cumul,couts_BU_cumul,last_cumul_BE, last_cumul_BU  = couts_cumulés(brevet_list)
    couts_BE_per_year,couts_BU_per_year= couts_année(brevet_list)
    list_year=liste_annees(brevet_list)
    return list_year,couts_BE_cumul,couts_BU_cumul, couts_BU_per_year,couts_BE_per_year,last_cumul_BE, last_cumul_BU
