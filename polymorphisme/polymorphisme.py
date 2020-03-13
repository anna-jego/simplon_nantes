# Polymorphisme
#     Ecrivez une classe Forme qui contiendra une méthode calculAire.
#     Faitesen hériter la classes Carre contenant un attribut cote
#     idem pour la classe Cercle contenant un attribut rayon.
#     Rédéfinir la méthode calculAire pour les classes Carre et Cercle
#     Définir une fonction AireTotal qui à partir d’un tableau de Forme calcul l’aire totale
import math


class Forme:
    def calcul_aire():
        pass


class Carre():
    def __init__(self, cote):
        self.cote = cote

    def calcul_aire(self):
        return self.cote ** 2


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return math.pi * self.rayon ** 2


cercle_1 = Cercle(1)
print('cercle_1 : ', cercle_1.calcul_aire())

carre_2 = Carre(2)
print('carre_2 : ', carre_2.calcul_aire())


# Polymorphisme
formes = [cercle_1, carre_2]
aire_totale = 0
for forme in formes:
    aire_totale += forme.calcul_aire()
print('Aire totale pour l\'ensemble des formes', aire_totale)
