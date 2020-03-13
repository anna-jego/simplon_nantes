# Création d'un programme qui joue de manière aléatoire

import os
import random
import time


def affiche(state, n):
    """
    Gestion d'un affichage graphique en console
    entrée:
        state : position de jeu sous la forme d'un tuple de 3 listes
                tour_1, tour_2, tour_3
        n :  nombre de disques
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for niveau in range(n, 0, -1):
        elt = ''
        for tower in state:
            if niveau <= len(tower):
                i = tower[niveau - 1]
                elt_temp = ' ' * (n - i) + '*' * \
                    (2 * (i - 1) + 1) + ' ' * (n - i) + ' '
                elt += elt_temp
            else:
                elt += ' ' * (2 * (n - 1) + 1) + ' '
        print(elt)
    legende = ' ' * (n - 1) + '1' + ' ' * (n - 1) + ' ' \
        + ' ' * (n - 1) + '2' + ' ' * (n - 1) + ' ' \
        + ' ' * (n - 1) + '3' + ' ' * (n - 1) + ' '
    print(legende)


def init(n):
    """
    Définition de la position initiale
    entrée:
        n :  nombre de disques
    sortie:
        state : position de jeu sous la forme d'un tuple de 3 listes
                tour_1, tour_2, tour_3
    """
    state = [i for i in range(n, 0, -1)], [], []
    return state


def available_moves(state):
    """
    Détermine l'ensemble des déplacements possibles pour une position donnée
    entrée:
        state
    sortie:
        liste de déplacements valides
        [move]
    """
    # >>> Début de votre code
    pass
    #     Fin de votre code <<<


def successor(state, move):
    """
    Détermine la position finale après le déplacement `move`
    qui respecte les règles
    entrée:
        state
        move
    sortie:
        state
    """
    start, end = move
    disk = state[start][-1]
    del state[start][-1]
    state[end].append(disk)

    return state


def is_end(state, n):
    """
    Vérification que la position est gagnante
    entrée:
        state
        n
    sortie:
        booléen
    """
    if len(state[2]) == n:
        return True
    else:
        return False


# Test des différentes fonctions

# Test de `available_moves`
# state = ([3, 2, 1], [], [])
# state = ([], [3, 2, 1], [])
# state = ([], [], [3, 2, 1])
# state = ([1], [], [3, 2])

# print(available_moves(state))

# Résultats:
# [(0, 1), (0, 2)]
# [(1, 0), (1, 2)]
# [(2, 0), (2, 1)]
# [(0, 1), (0, 2), (2, 1)]


# ### Le jeu ####

# n = 3
# state = init(n)

# affiche(state, n)

# while not is_end(state, n):
#     time.sleep(0.1)
#     # >>> Début de votre code
#     pass
#     #     Fin de votre code <<<

# print("Gagné")
