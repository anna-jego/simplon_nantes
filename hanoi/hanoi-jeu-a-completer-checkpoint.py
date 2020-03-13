
def init(n):
    """
    Définition de la position initiale
    entrée:
        n :  nombre de disques
    sortie:
        state : position de jeu sous la forme d'un tuple de 3 listes
                tour_1, tour_2, tour_3
    """
    # >>> Début de votre code
    pass
    #     Fin de votre code <<<


def is_valid(state, move):
    """
    On s'assure que pour la position `state` donnée
    le déplacement `move` respecte bien les règles
    entrée:
        state
        move est un tuple de deux entiers:
            start, end
    sortie:
        booléen
    """

    # >>> Début de votre code
    pass

    # On vérifie que la tour initiale n'est pas vide
    # On vérifie que le disque sur lequel on pose le disque déplacé
    # est bien plus grand
    # Les coordonnées des tours seront validées dans l'interface du jeu

    #     Fin de votre code <<<


def successor(state, move):
    """
    Détermine la position finale après le déplacement `move`
    entrée:
        state
        move
    sortie:
        state
    """
    # >>> Début de votre code
    pass
    #     Fin de votre code <<<


def is_end(state, n):
    """
    Vérification que la position est gagnante
    entrée:
        state
        n
    sortie:
        booléen
    """
    # >>> Début de votre code
    pass
    #     Fin de votre code <<<

# ###### Test des différentes fonctions ##### #
# state = init(3)
# print(state)
# # ([3, 2, 1], [], [])

# state = init(3)
# move = (0, 2)
# state = successor(state, move)
# print(state)
# # ([3, 2], [], [1])

# state = init(3)
# move = (0, 2)
# state = successor(state, move)
# move = (0, 2)
# state = successor(state, move)
# # "Déplacement non valide"

# state = [], [], [3, 2, 1]
# print(is_end(state, 3))
# # True


# ###### Le jeu ##### #

# Devra comporter entre autre les éléments suivants
# Interface utilisateur
# Vérification de la cohérence des entrées
# Détermination de la position suivante

# >>> Début de votre code
pass
#     Fin de votre code <<<
