USE biblioTP02;
/*
SERIE 2 : La bibliothèque - Requêtes

1.    Quels sont les livres actuellement empruntés ?
*/
SELECT * FROM emprunter;

SELECT * FROM emprunter WHERE dateRet IS NULL;
    
/*
2.    Quels sont les livres empruntés par Jeannette Lecoeur ? Vérifier dans la réponse qu’il n’y a pas d’homonymes.
*/
select * from adherents where nom = "Lecoeur" and prenom = "Jeannette";

select * from adherents
where nom = "Lecoeur";
-- Il y a bien une Jeannette Lecoeur mais avec un seul n
select * from adherents
where nom = "Lecoeur" and prenom = "Jeanette";
-- NA: 1
select * from emprunter
where na = 1;

/*
3.    Quels sont tous les livres empruntés le mois dernier ?
*/
-- Le mois en cours
select month(curdate()) as mois, year(curdate()) as annee;
-- -1 mois
select * from emprunter
where month(datEmp) = month(curdate() - interval 1 month)
and year(datEmp) = year(curdate() - interval 1 month);
