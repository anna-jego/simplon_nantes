# Version sans décorateurs


class TableauTrieAbstrait:
    """
    classe abstraite destinée à gérer un tableau d'éléments triés
    """

    def __init__(self):
        self.tableau = []  # Tableau stocké sous la forme d'une liste

    def __repr__(self):
        return str(self.tableau)

    def plus_grand(self, a, b):
        """
        Méthode abstraite
        """
        raise NotImplementedError(
        )  # On s'assure que toutes les classes filles implémentent cette méthode

    def inserer(self, element):
        """
        Méthode commune d'insersion d'un élément dans le tableau
        On compare notre élément à toutes les valeurs du tableau par ordre croissant
        On l'insère dès que élément < valeur[tableau]
        """
        nouveau_tableau = []

        # >>> Début de votre code

        # Les premières valeurs du tableau

        # L'élément en question

        # Les dernières valeurs du tableau

        #     Fin de votre code <<<

        self.tableau = nouveau_tableau


class TableauTrieEntiers(TableauTrieAbstrait):
    def plus_grand(self, a, b):
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


class TableauTrieChaines(TableauTrieAbstrait):
    def plus_grand(self, a, b):
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


tableau_trie_d_entiers = TableauTrieEntiers()
print(tableau_trie_d_entiers)
tableau_trie_d_entiers.inserer(5)
print(tableau_trie_d_entiers)
tableau_trie_d_entiers.inserer(2)
print(tableau_trie_d_entiers)
tableau_trie_d_entiers.inserer(3)
print(tableau_trie_d_entiers)
tableau_trie_d_entiers.inserer(6)
print(tableau_trie_d_entiers)
tableau_trie_d_entiers.inserer(1)
print(tableau_trie_d_entiers)

tableau_trie_de_chaines = TableauTrieChaines()
tableau_trie_de_chaines.inserer('cool')
tableau_trie_de_chaines.inserer('ce')
tableau_trie_de_chaines.inserer('ici')
tableau_trie_de_chaines.inserer('a')
tableau_trie_de_chaines.inserer('suite')
print(tableau_trie_de_chaines)
