# Micro-monde économique de la boulangerie
# Pas d'utilisation des décorateurs pour définir les classes
# et méthodes abstraites


class Produit:  # Classe abstraite
    def __init__(self):
        self.quantite = 0
        self._type = 'Produit non défini'  # Attribut protégé

    def __repr__(self):
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


class Pain(Produit):
    def __init__(self, quantite):
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


class Personnage:  # Classe abstraite
    def __init__(self):
        # Chaque personnage commence le jeu avec 2 pains
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<

    def manger(self):
        """
        Renvoie:
        Vrai si le personnage a reussi à manger
        Faux si personnage n'a pas pu manger
        """
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


class Paysan(Personnage):
    pass

    # ### Programme Principal ### #
# pain = Pain(2)
# print(pain)


paysan = Paysan()
# Faire manger le paysan tant qu'il y a du pain
# J'ai bien mangé
# Pain restant :  1
# J'ai bien mangé
# Pain restant :  0
# J'ai faim
