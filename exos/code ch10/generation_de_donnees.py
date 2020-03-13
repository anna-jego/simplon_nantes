#-----------------------------------------------------------------------------------------
# @Auteur : Aurélien Vannieuwenhuyze
# @Entreprise : Junior Makers Place
# @Livre :
# @Chapitre : 10 - Entre abricots et cerise : une histoire de clustering
#
# Modules necessaires :
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#   SCIKIT-LEARN : 0.21.0
#   MATPLOTLIB : 3.0.3
#   JOBLIB : 0.13.2
#
# Pour installer un module :
#   Cliquer sur le menu File > Settings > Project:nom_du_projet > Project interpreter > bouton +
#   Dans la zone de recherche en haut à gauche saisir le nom du module
#   Choisir la version en bas à droite
#   Cliquer sur le bouton install situé en bas à gauche
#-----------------------------------------------------------------------------------------



#---- IMPORT DES MODULES --
import random
import pandas as pnd

#---- CARACTERISTIQUES------

#CERISES
caracteristiquesCerises = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]



#ABRICOTS : ATTENTION DEUX CAS DE TESTS EN FONCTION DE L'AVANCEE DE VOTRE LECTURE

#Cas 1 :
caracteristiquesAbricots = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]

#Cas 2 :
#caracteristiquesAbricots = [[35,39,27],[40,44,41],[45,49,54],[50,54,74],[55,59,100]]


#GENERATION DES DONNEES
# [DIAMETRE, POIDS]
nombreObservations = 200

#Generation des cerises
cerises = []
random.seed()
for iteration in range(nombreObservations):
    #choix au hazard d'une caracteristique
    cerise = random.choice(caracteristiquesCerises)
    #Generation d'un diametre
    diametre = round(random.uniform(cerise[0], cerise[1]),2)
    #Generation d'un poids
    poids = round(random.uniform(cerise[2], cerise[3]),2)
    print ("Cerise "+str(iteration)+" "+str(cerise)+" : "+str(diametre)+" - "+str(poids))
    cerises.append([diametre,poids])


#Generation des abricots
abricots = []
random.seed()
for iteration in range(nombreObservations):
    #choix au hazard d'une caracteristique
    abricot = random.choice(caracteristiquesAbricots)
    #Generation d'un diametre
    diametre = round(random.uniform(abricot[0], abricot[1]),2)
    #Generation d'un poids
    borneMinPoids = abricot[2] / 1.10
    borneMaxPoids = abricot[2] * 1.10
    poids = round(random.uniform(borneMinPoids, borneMaxPoids),2)
    print ("Abricot "+str(iteration)+" "+str(abricot)+" : "+str(diametre)+" - "+str(poids))
    abricots.append([diametre,poids])


#Constitution des observations
fruits = cerises+abricots
print(fruits)

#Mélange des observations
random.shuffle(fruits)

#Sauvegarde des observations dans un fichier
dataFrame = pnd.DataFrame(fruits)
dataFrame.to_csv("datas/fruits.csv", index=False,header=False)






