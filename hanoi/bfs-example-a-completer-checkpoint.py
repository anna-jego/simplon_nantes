# BFS example
# Breadth First Search
# Parcours en largeur

# On fournit un sommet de départ s
# et la "liste" d'adjacence: Adjency list (adj)


def bfs(s, adj):
    level = {s: 0}  # Niveau de profondeur de la recherche
    parent = {s: None}  # parent du sommet
    i = 1
    frontier = [s]  # Liste représentant la frontière en cours d'exploration
    while frontier:
        next_frontier = []  # Prochaine frontière visible
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next_frontier.append(v)
        frontier = next_frontier
        i += 1


# Graphe étudié
#  a - s   d - f
#  |   | / | / |
#  z   x - c - t

# Définir le dictionnaire des adjacences
# >>> Début de votre code
pass
#     Fin de votre code <<<

# Afficher les frontières de différents niveaux
# en appelant la fontion bfs
# "Frontière niveau  1  :  ..."

# >>> Début de votre code
pass
#     Fin de votre code <<<

# intervertir t et d
# Modifier la fonction pour qu'elle s'arrêtre dès qu'on atteind t
# >>> Début de votre code
pass
#     Fin de votre code <<<
