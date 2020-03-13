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



import pandas as pnd
import matplotlib.pyplot as plt


#Chargement des données
fruits = pnd.read_csv("datas/fruits.csv", names=['DIAMETRE','POIDS'], header=None)

#Visualisation graphique des données
fruits.plot.scatter(x="DIAMETRE",y="POIDS")
plt.show()


#Apprentissage avec l'algorithme K-Mean
from sklearn.cluster import KMeans
modele=KMeans(n_clusters=2)
modele.fit(fruits)

#Predictions
predictions_kmeans = modele.predict(fruits)

#Affichage de la clusterisation
plt.scatter(fruits.DIAMETRE, fruits.POIDS, c=predictions_kmeans, s=50, cmap='viridis')
plt.xlabel("DIAMETRE")
plt.ylabel("POIDS")

#Affichage des centroïdes
centers = modele.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()

#Sauvegarde du modèle ( A décommenter si besoin)
#from joblib import dump
#dump(modele,'modeles/kmean.joblib')

#--- Realisation de classifications --
#CERISE: 26.98 mm de diametre ,8.75 grammes
#ABRICOT: 55.7  mm de diametre , 102.16 grammes


cerise = [[26.98,8.75]]
numCluster = modele.predict(cerise)
print("Numero de cluster des cerises: "+ str(numCluster))


abricot = [[55.7,102.16]]
numCluster = modele.predict(abricot)
print("Numero de cluster des abricots: " + str(numCluster))

#Code à adapter en fonction des numéros de clusters
#déterminés précédemment :

cerise = [[26.98,8.75]]
numCluster = modele.predict(cerise)
if int(numCluster)==0:
    print("C'est un abricot !")
else:
    print("C'est une cerise ! ")


abricot = [[55.7,102.16]]
numCluster = modele.predict(abricot)
if int(numCluster)==0:
    print("C'est un abricot !")
else:
    print("C'est une cerise ! ")


#---- Modele de mélanges Gaussiens (GMM) -----------
from sklearn import mixture

#Détermination des clusters (2 à trouver)
gmm = mixture.GaussianMixture(n_components=2)

#Apprentissage
gmm.fit(fruits)

#Classification
clusters = gmm.predict(fruits)

#Affichage des clusters
plt.scatter(fruits.DIAMETRE, fruits.POIDS, c=clusters, s=40, cmap='viridis');
plt.xlabel("DIAMETRE")
plt.ylabel("POIDS")
plt.show()

