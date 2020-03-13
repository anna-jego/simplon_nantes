#-----------------------------------------------------------------------------------------
# @Auteur : Aurélien Vannieuwenhuyze
# @Entreprise : Junior Makers Place
# @Livre :
# @Chapitre : 13 - Classification d'images
#
# Modules necessaires :
#   TENSORFLOW 1.13.1
#   KERAS 2.2.4
#   OPENCV 3.4.5.20
#   PYTTSX3 2.7.1
#   SCIKIT-LEARN 0.21.1
#   NUMPY 1.16.3
#
# Pour installer un module :
#   Cliquer sur le menu File > Settings > Project:nom_du_projet > Project interpreter > bouton +
#   Dans la zone de recherche en haut à gauche saisir le nom du module
#   Choisir la version en bas à droite
#   Cliquer sur le bouton install situé en bas à gauche
#-----------------------------------------------------------------------------------------


from __future__ import print_function
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split

from mnist import MNIST


#Chargement des images
emnist_data = MNIST(path='datas\\', return_type='numpy')
emnist_data.select_emnist('letters')
Images, Libelles = emnist_data.load_training()


print("Nombre d'images ="+str(len(Images)))
print("Nombre de libellés ="+str(len(Libelles)))



#Conversion des images et libellés en tableau numpy
import numpy as np
Images = np.asarray(Images)
Libelles = np.asarray(Libelles)


#Dimension des images de travail et d'apprentissage
longueurImage = 28
largeurImage = 28


#Les images sont sous forme d'un tableau de 124800 lignes et 784 colonnes
#On les transforme en un tableau comportant 124800 lignes contenant un tableau de 28*28 colonnes
print("Transformation des tableaux d'images...")
Images = Images.reshape(124800, largeurImage, longueurImage)
Libelles= Libelles.reshape(124800, 1)

print("Affichage de l'image N°70000...")
from matplotlib import pyplot as plt
plt.imshow(Images[70000])
plt.show()

print(Libelles[70000])

#En informatique, les index des listes doivent commencer à zéro...")
Libelles = Libelles-1


print("Libellé de l'image N°70000...")
print(Libelles[70000])



#Création des jeux d'apprentissage et de test
images_apprentissage, images_validation, libelles_apprentissage, libelles_validation = train_test_split(Images, Libelles, test_size=0.25, random_state=42)

#Ajout d'une troisième valeur à nos tableaux d'images pour pouvoir être utilisés par le réseau de neurones, notemment le paramètre input_shape de la fonction Conv2D
images_apprentissage = images_apprentissage.reshape(images_apprentissage.shape[0], largeurImage, longueurImage, 1)
print(images_apprentissage.shape)

images_validation = images_validation.reshape(images_validation.shape[0], largeurImage, longueurImage, 1)

#Création d'une variable servant de d'image de travail au réseau de neurone
imageTravail = (largeurImage, longueurImage, 1)

#Mise à l'echelle 
images_apprentissage = images_apprentissage.astype('float32')/255
images_validation = images_validation.astype('float32')/255

# Creation des categories en One-Hot encoding
nombre_de_classes = 26
libelles_apprentissage = keras.utils.to_categorical(libelles_apprentissage, nombre_de_classes)
libelles_validation = keras.utils.to_categorical(libelles_validation, nombre_de_classes)

# Réseau de neurone convolutif
# 32 filtres de dimensions 3x3 avec une fonction d'activation de type RELU
# Le filtre a en entree l'image de travail
reseauCNN = Sequential()
reseauCNN.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=imageTravail))

#Un seconde couche de 64 filtres de dimension 3x3
reseauCNN.add(Conv2D(64, (3, 3), activation='relu'))

#Une fonction de pooling
reseauCNN.add(MaxPooling2D(pool_size=(2, 2)))
reseauCNN.add(Dropout(0.25))

#Une mise à plat
reseauCNN.add(Flatten())

#Le réseau de neurone avec en entrée 128 neurones
#une fonction d'activation de type ReLU
reseauCNN.add(Dense(128, activation='relu'))
reseauCNN.add(Dropout(0.5))

#Une dernière couche de type softmax
reseauCNN.add(Dense(nombre_de_classes, activation='softmax'))

#Compilation du modèle
reseauCNN.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])


# Apprentissage avec une phase de validation
# sur les jeux de test
batch_size = 128
epochs = 10

reseauCNN.fit(images_apprentissage, libelles_apprentissage,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(images_validation, libelles_validation))



# Sauvegarde du modèle
reseauCNN.save('modele/modele_cas_pratiquev2.h5')

# Evaluation de la précision du modèle
score = reseauCNN.evaluate(images_validation, libelles_validation, verbose=0)
print('Precision sur les donnees de validation:', score[1])