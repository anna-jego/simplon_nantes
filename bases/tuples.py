





Les tuples sont des listes, mais celles-ci sont NON MODIFIABLES, ce sont des collections d’éléments, 
mais leurs éléments sont fixés; càd, qu'une fois le tuple est créé, 
vous ne pouvez pas ajouter de nouveaux éléments, supprimer des éléments, remplacer des éléments, 
ou réorganiser les éléments du tuple.

Si le contenu d’une liste dans votre programme/fonction ne devrait pas changer, vous pouvez utiliser 
un tuple pour éviter que des éléments soient ajoutés, supprimés ou remplacés accidentellement.

#La vocation de ce type de liste est d'être utilisé à titre de constante dans l'application.

Créer un tuple :

Pour créer un tuple , on peut utiliser la syntaxe suivante: 

exemple : 

>>> mon_tuple = ()

Si l'on souhaite ajouter une valeur à un tuple ça sera de cette façon: 

exemple : 

>>> mon_tuple = (1, "ok", "salut")

#Les parenthèses ne sont pas obligatoires mais facilite la lisibilité du code : 


exemple : 

>>> mon_tuple = 1, 2, 3
>>> type(mon_tuple)
<type 'tuple'>

Attention, lorsqu'on veut créer un tuple avec 1 seule valeur, il est impératif d'y ajouter une virgule (sinon ce n'est pas un tuple). 

exemple :

>>> mon_tuple = ("ok")
>>> type(mon_tuple)
<type 'str'>
>>> mon_tuple = ("ok",)
>>> type(mon_tuple)
<type 'tuple'>

Comme le tuple est une liste, on utilisera la même syntaxe pour lire les données du tuple. 

exemple : 

>>> mon_tuple[0]
1

A quoi sert un tuple alors? 

Le tuple permet une affectation multiple: 
>>> v1, v2 = 11, 22
>>> v1
11
>>> v2
22

Il permet également de renvoyer plusieurs valeurs lors d'un appel d'une fonction: 
>>> def donne_moi_ton_nom():
...     return "anna", "jégo"
... 
>>> donne_moi_ton_nom()
('anna', 'jégo')

On utilisera un tuple pour définir des sortes de constantes qui n'ont donc pas vocation à changer. 

Pour résumer : 

t1 = () # Crée un tuple vide
t2 = (1, 3, 5) # Crée un tuple constitué de trois éléments
t3 = (2,) # Crée un tuple constitué d’un seul élément
# Crée un tuple à partir d’une liste
t3 = tuple([2 * x for x in range(1, 5)])
# Créer un tuple à partir d'une chaîne de caractères
t4 = tuple("abac") 
t4 est ('a', 'b', 'a', 'c')