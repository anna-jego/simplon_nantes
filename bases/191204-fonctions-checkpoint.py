# Résumé sur les fonctions


# def fonction_vide():
#     pass


# Appel à une fonction
# print(fonction_vide)
# print(fonction_vide())  # pour exécuter la fonction


# def fonction_bonjour():
#     print("Bonjour ...")


# fonction_bonjour()
# fonction_bonjour()
# fonction_bonjour()
# fonction_bonjour()

# print("Bonjour ...")
# print("Bonjour ...")
# print("Bonjour")
# print("Bonjour ...")

# def fonction_bonjour():
#     return "Bonjour !"


# fonction_bonjour()
# print(fonction_bonjour())
# print(fonction_bonjour().upper())


# Passage d'arguments à la fonction
# def salutation(nom_dans_fonction):
#     chaine_a_renvoyer = 'Bonjour ' + nom_dans_fonction
#     return chaine_a_renvoyer


# print(salutation())

# print(salutation('Audrey'))
# print(salutation('Daouda'))

# nom_dans_prog_principal = 'Gaspard'
# print(salutation(nom_dans_prog_principal))

# Passage d'arguments à la fonction avec valeur par défaut
# def salutation(nom_dans_fonction='humain'):
#     chaine_a_renvoyer = 'Bonjour ' + nom_dans_fonction
#     return chaine_a_renvoyer


# print(salutation())
# print(salutation('Daouda'))

# Même nom mais pas la même chose
# def salutation(nom):
#     print('nom dans fonction: ', nom)

#     chaine_a_renvoyer = 'Bonjour ' + nom
#     return chaine_a_renvoyer


# nom = 'Kévan'
# print(salutation(nom))
# print('nom dans prog principal: ', nom)

# print('---')
# print(salutation('Minwei'))
# print('nom dans prog principal: ', nom)


# Plusieurs arguments
# def saluer(salutation, nom):
#     return salutation + ' ' + nom

# print(saluer('Bonjour', 'Rijarivo'))
# print(saluer('Salut', 'Manon'))


# def info_apprenant(*arg, **karg):
#     print(arg)
#     print(karg)


# info_apprenant('Python', 'SQL', 'IA', nom='Ousmane', age=22)


# # Année bissextile?
# def est_bissextile(annee):
#     pass

# # Nombre de jours dans le mois
# def nombre_de_jours(mois,annee):
#     pass


# print(nombre_de_jours(2,2020))
# print(nombre_de_jours(3,2020))
# print(nombre_de_jours(2,2019))
