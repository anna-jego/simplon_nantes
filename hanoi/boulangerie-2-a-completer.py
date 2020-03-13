# Micro-monde économique de la boulangerie
# Gestion des réceptions de produits


class Produit:  # Classe abstraite
    def __init__(self):
        self.quantite = 0
        # 3 types de produits possibles
        #     Farine
        #     Blé
        #     Pain
        self._type = 'Produit non défini'  # Attribut protégé

    def __repr__(self):
        return self._type + ' : ' + str(self.quantite)


class Pain(Produit):
    def __init__(self, quantite=0):
        self.quantite = quantite
        self._type = 'Pain'  # Attribut protégé


class Ble(Produit):
    def __init__(self, quantite=0):
        Produit.__init__(self)
        self.quantite = quantite
        self._type = 'Blé'  # Attribut protégé


class Farine(Produit):
    def __init__(self, quantite=0):
        Produit.__init__(self)
        self.quantite = quantite
        self._type = 'Farine'  # Attribut protégé


class Personnage:  # Classe abstraite
    def __init__(self):
        # Tous les personnages peuvent posséder du pain
        self.pain = Pain()

    def manger(self):
        if self.pain.quantite > 0:
            self.pain.quantite -= 1
            return True  # Mon personnage a reussi à manger
        else:
            return False  # Mon personnage n'a pas pu manger

    def produire(self):  # Méthode abstraite
        raise NotImplementedError()

    def recevoir(self, produit):  # Méthode abstraite
        raise NotImplementedError()

    def livrer(self, produit, personnage):  # Méthode abstraite
        raise NotImplementedError()


class Paysan(Personnage):
    def __init__(self):
        Personnage.__init__(self)
        self.ble = Ble()

    def __repr__(self):
        representation = 'Paysan' + '\n\t' + \
            repr(self.pain) + '\n\t' +\
            repr(self.ble)
        return representation

    def produire(self):
        """
        Le Paysan produit du blé
        On considère que c'est toujours possible
        """
        self.ble.quantite += 1
        return True

    def recevoir(self, produit):
        """
        Le paysan ne peut recevoir que du pain
        """
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


class Meunier(Personnage):
    def __init__(self):
        Personnage.__init__(self)
        self.farine = Farine()
        self.ble = Ble()

    def __repr__(self):
        representation = 'Meunier' + '\n\t' + \
            repr(self.pain) + '\n\t' +\
            repr(self.ble) + '\n\t' +\
            repr(self.farine)
        return representation

    def produire(self):
        """
        Le meunier produit de la farine s'il a du blé
        renvoie: True s'il a pu produire
                 False sinon
        """
        if self.ble.quantite > 0:
            self.farine.quantite += 1
            self.ble.quantite -= 1
            return True
        else:
            return False

    def recevoir(self, produit):
        """
        Le meunier peut recevoir du pain ou du blé
        """
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<


class Boulanger(Personnage):
    def __init__(self):
        Personnage.__init__(self)
        self.farine = Farine()

    def __repr__(self):
        representation = 'Boulanger' + '\n\t' + \
            repr(self.pain) + '\n\t' +\
            repr(self.farine)
        return representation

    def produire(self):
        """
        Le boulanger produit du pain s'il a de la farine
        renvoie: True s'il a pu produire
                 False sinon
        """
        if self.farine.quantite > 0:
            self.pain.quantite += 1
            self.farine.quantite -= 1
            return True
        else:
            return False

    def recevoir(self, produit):
        """
        Le boulanger peut recevoir du pain ou de la farine
        """
        # >>> Début de votre code
        pass
        #     Fin de votre code <<<

# ### Programme Principal ### #


paysan = Paysan()
print(paysan)

pain_a_livrer = Pain(2)
print(pain_a_livrer)

paysan.recevoir(pain_a_livrer)
print(paysan)

# Test si on livre autre chose au paysan

# Test réception meunier

# Test réception boulanger
