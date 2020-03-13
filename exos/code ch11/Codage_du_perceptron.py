#-----------------------------------------------------------------------------------------
# @Auteur : Aurélien Vannieuwenhuyze
# @Entreprise : Junior Makers Place
# @Livre :
# @Chapitre : 10 - Entre abricots et cerise : une histoire de clustering
#
# Modules necessaires :
#   NUMPY 1.16.3
#   MATPLOTLIB : 3.0.3
#   TENSORFLOW : 1.13.1
#
# Pour installer un module :
#   Cliquer sur le menu File > Settings > Project:nom_du_projet > Project interpreter > bouton +
#   Dans la zone de recherche en haut à gauche saisir le nom du module
#   Choisir la version en bas à droite
#   Cliquer sur le bouton install situé en bas à gauche
#-----------------------------------------------------------------------------------------


from numpy import exp, array, random

#-------------------------------------
#    OBSERVATIONS ET PREDICTIONS
#-------------------------------------

observations_entrees = array([
                              [1, 0],
                              [1, 1],
                              [0, 1],
                              [0, 0]
                              ])


predictions = array([[0],[1], [0],[0]])


#--------------------------------------
#        PARAMETRAGE DU PERCEPTRON
#--------------------------------------

#Génération des poids dans l'interval [-1;1]
random.seed(1)
borneMin = -1
borneMax = 1

w11 = (borneMax-borneMin) * random.random() + borneMin
w21 = (borneMax-borneMin) * random.random() + borneMin
w31 = (borneMax-borneMin) * random.random() + borneMin

#Le biais
biais = 1
wb = 0

#Stockage des poids initiaux, uniquement pour affichage à la fin de l'apprentissage
poids = [w11,w21,w31,wb]

#Taux d'apprentissage
txApprentissage = 0.1

#Nombres d'epoques
epochs = 300000


#--------------------------------------
#       FONCTIONS UTILES
#--------------------------------------


def somme_ponderee(X1,W11,X2,W21,B,WB):
    return (B*WB+( X1*W11 + X2*W21))

def fonction_activation_sigmoide(valeur_somme_ponderee):
    return (1 / (1 + exp(-valeur_somme_ponderee)))

def fonction_activation_relu(valeur_somme_ponderee):
    return (max(0,valeur_somme_ponderee))

def erreur_lineaire(valeur_attendue, valeur_predite):
    return (valeur_attendue-valeur_predite)

def calcul_gradient(valeur_entree,prediction,erreur):
    return (-1 * erreur * prediction * (1-prediction) * valeur_entree)

def calcul_valeur_ajustement(valeur_gradient, taux_apprentissage):
    return (valeur_gradient*taux_apprentissage)

def calcul_nouveau_poids (valeur_poids, valeur_ajustement):
    return (valeur_poids - valeur_ajustement)

def calcul_MSE(predictions_realisees, predictions_attendues):
    i=0;
    somme=0;
    for prediction in predictions_attendues:
        difference = predictions_attendues[i] - predictions_realisees[i]
        carreDifference = difference * difference
        somme = somme + carreDifference
    moyenne_quadratique = 1 / (len(predictions_attendues)) * somme
    return moyenne_quadratique


#--------------------------------------
#       GRAPHIQUE
#--------------------------------------

Graphique_MSE=[]


#--------------------------------------
#    APPRENTISSAGE
#--------------------------------------

for epoch in range(0,epochs):
    print("EPOCH ("+str(epoch)+"/"+str(epochs)+")")
    predictions_realisees_durant_epoch = [];
    predictions_attendues = [];
    numObservation = 0
    for observation in observations_entrees:

        #Chargement de la couche d'entrée
        x1 = observation[0];
        x2 = observation[1];

        #Valeur de prédiction attendue
        valeur_attendue = predictions[numObservation][0]

        #Etape 1 : Calcul de la somme ponderee
        valeur_somme_ponderee = somme_ponderee(x1,w11,x2,w21,biais,wb)


        #Etape 2 : Application de la fonction d'activation
        valeur_predite = fonction_activation_sigmoide(valeur_somme_ponderee)


        #Etape 3 : Calcul de l'erreur
        valeur_erreur = erreur_lineaire(valeur_attendue,valeur_predite)


        #Mise à jour du poids 1
        #Calcul du gradient de la valeur d'ajustement et du nouveau poids
        gradient_W11 = calcul_gradient(x1,valeur_predite,valeur_erreur)
        valeur_ajustement_W11 = calcul_valeur_ajustement(gradient_W11,txApprentissage)
        w11 = calcul_nouveau_poids(w11,valeur_ajustement_W11)

        # Mise à jour du poids 2
        gradient_W21 = calcul_gradient(x2, valeur_predite, valeur_erreur)
        valeur_ajustement_W21 = calcul_valeur_ajustement(gradient_W21, txApprentissage)
        w21 = calcul_nouveau_poids(w21, valeur_ajustement_W21)


        # Mise à jour du poids du biais
        gradient_Wb = calcul_gradient(biais, valeur_predite, valeur_erreur)
        valeur_ajustement_Wb = calcul_valeur_ajustement(gradient_Wb, txApprentissage)
        wb = calcul_nouveau_poids(wb, valeur_ajustement_Wb)

        print("     EPOCH (" + str(epoch) + "/" + str(epochs) + ") -  Observation: " + str(numObservation+1) + "/" + str(len(observations_entrees)))

        #Stockage de la prediction realisee:
        predictions_realisees_durant_epoch.append(valeur_predite)
        predictions_attendues.append(predictions[numObservation][0])

        #Passage à l'observation suivante
        numObservation = numObservation+1

    MSE = calcul_MSE(predictions_realisees_durant_epoch, predictions)
    Graphique_MSE.append(MSE[0])
    print("MSE : "+str(MSE))



import matplotlib.pyplot as plt
plt.plot(Graphique_MSE)
plt.ylabel('MSE')
plt.show()


print()
print()
print ("Apprentissage terminé !")
print ("Poid initiaux: " )
print ("W11 = "+str(poids[0]))
print ("W21 = "+str(poids[1]))
print ("Wb = "+str(poids[3]))

print ("Poid finaux: " )
print ("W11 = "+str(w11))
print ("W21 = "+str(w21))
print ("Wb = "+str(wb))

print()
print("--------------------------")
print ("PREDICTION ")
print("--------------------------")
x1 = 1
x2 = 1

#Etape 1 : Calcul de la somme ponderee
valeur_somme_ponderee = somme_ponderee(x1,w11,x2,w21,biais,wb)


#Etape 2 : Application de la fonction d'activation
valeur_predite = fonction_activation_sigmoide(valeur_somme_ponderee)
#valeur_predite = fonction_activation_relu(valeur_somme_ponderee)

print("Prediction du [" + str(x1) + "," + str(x2)  + "]")
print("Prediction = " + str(valeur_predite))


