#-----------------------------------------------------------------------------------------
# @Auteur : Aurélien Vannieuwenhuyze
# @Entreprise : Junior Makers Place
# @Livre :
# @Chapitre : 11 - Un neurone pour prédire
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




#-------------------------------------
#    PARAMETRES GENERAUX
#-------------------------------------

valeurs_entrees_X = [[1., 0.], [1., 1.], [0., 1.], [0., 0.]]
valeurs_a_predire_Y = [[0.], [1.], [0.], [0.]]



#-------------------------------------
#    PARAMETRES DU RESEAU
#-------------------------------------
import tensorflow as tf


#Variable TensorFLow correspondant aux valeurs neurones d'entrée
tf_neurones_entrees_X = tf.placeholder(tf.float32, [None, 2])

#Variable TensorFlow correspondant au neurone de sortie (prédiction reele)
tf_valeurs_reelles_Y = tf.placeholder(tf.float32, [None, 1])

#-- Poids --
#Création d'une variable TensorFlow de type tableau
#contenant 2 entrées ayant chacune un 1 poids [2,1]
#Ces valeurs sont initialisées aux hasard
poids = tf.Variable(tf.random_normal([2, 1]), tf.float32)

#-- Biais initialisée à 0 --
biais = tf.Variable(tf.zeros([1, 1]), tf.float32)

#La somme pondérée est en fait une multiplication de matrice
#entre les valeur en entrées X et les différents poids
#la fonction matmul se charge de faire cette multiplication
sommeponderee = tf.matmul(tf_neurones_entrees_X,poids)

#Ajout du biais à la somme ponderee
sommeponderee = tf.add(sommeponderee,biais)

#Fonction d'activation de type sigmoide permettant de calculer la prédiction
prediction = tf.sigmoid(sommeponderee)

#Fonction d'erreur de moyenne quadratique MSE
fonction_erreur = tf.reduce_sum(tf.pow(tf_valeurs_reelles_Y-prediction,2))

#Descente de gradient avec un taux d'apprentissage fixé à 0.1
optimiseur = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(fonction_erreur)



#-------------------------------------
#    APPRENTISSAGE
#-------------------------------------

#Nombre d'epochs
epochs = 10000

#Initialisation des variable
init = tf.global_variables_initializer()

#Demarrage d'une session d'apprentissage
session = tf.Session()
session.run(init)

#Pour la réalisation du graphique pour la MSE
Graphique_MSE=[]


#Pour chaque epoch
for i in range(epochs):

   #Realisation de l'apprentissage avec mise à jour des poids
   session.run(optimiseur, feed_dict = {tf_neurones_entrees_X: valeurs_entrees_X, tf_valeurs_reelles_Y:valeurs_a_predire_Y})

   #Calculer l'erreur
   MSE = session.run(fonction_erreur, feed_dict = {tf_neurones_entrees_X: valeurs_entrees_X, tf_valeurs_reelles_Y:valeurs_a_predire_Y})

   #Affichage des informations
   Graphique_MSE.append(MSE)
   print("EPOCH (" + str(i) + "/" + str(epochs) + ") -  MSE: "+ str(MSE))


#Affichage graphique
import matplotlib.pyplot as plt
plt.plot(Graphique_MSE)
plt.ylabel('MSE')
plt.show()

print("--- VERIFICATIONS ----")

for i in range(0,4):
    print("Observation:"+str(valeurs_entrees_X[i])+ " - Attendu: "+str(valeurs_a_predire_Y[i])+" - Prediction: "+str(session.run(prediction, feed_dict={tf_neurones_entrees_X: [valeurs_entrees_X[i]]})))



session.close()
