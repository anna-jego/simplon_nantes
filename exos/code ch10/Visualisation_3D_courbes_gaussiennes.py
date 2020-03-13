
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
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

fruits = pnd.read_csv("datas/fruits.csv", names=['DIAMETRE','POIDS'], header=None)

n_components = 2


# Extract x and y
x = fruits.DIAMETRE
y = fruits.POIDS
# Define the borders
deltaX = (max(x) - min(x))/10
deltaY = (max(y) - min(y))/10
xmin = min(x) - deltaX
xmax = max(x) + deltaX
ymin = min(y) - deltaY
ymax = max(y) + deltaY
print(xmin, xmax, ymin, ymax)
# Create meshgrid
xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]

positions = np.vstack([xx.ravel(), yy.ravel()])
values = np.vstack([x, y])
kernel = st.gaussian_kde(values)
f = np.reshape(kernel(positions).T, xx.shape)

fig = plt.figure(figsize=(8,8))
ax = fig.gca()
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
cfset = ax.contourf(xx, yy, f, cmap='coolwarm')
ax.imshow(np.rot90(f), cmap='coolwarm', extent=[xmin, xmax, ymin, ymax])
cset = ax.contour(xx, yy, f, colors='k')
ax.clabel(cset, inline=1, fontsize=10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()

from mpl_toolkits.mplot3d import axes3d, Axes3D
fig = plt.figure(figsize=(13, 7))
ax = plt.axes(projection='3d')
surf = ax.plot_surface(xx, yy, f, rstride=1, cstride=1, cmap='coolwarm', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.colorbar(surf, shrink=0.5, aspect=5) # add color bar indicating the PDF
ax.view_init(60, 35)
plt.show()