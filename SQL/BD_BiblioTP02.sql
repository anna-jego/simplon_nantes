-- Fichier texte encodé en UTF8 with BOM : vérifiez que les accents sont propres dans la BD

-- Création de la BD  : on supprime la database, on la recrée, on l'utilise
-- remarque : WAMP interdit l'utilisation du drop database : il faut faire ça dans une calculette.

drop database if exists biblioTP02;
create database biblioTP02;

use biblioTP02;

CREATE TABLE oeuvres(
  NO        integer primary key auto_increment,
  titre     varchar(150),
  auteur    varchar(100)
) ENGINE InnoDB;

CREATE TABLE adherents (
  NA        int PRIMARY KEY AUTO_INCREMENT,
  nom       varchar(30) not null,
  prenom    varchar(30),
  adr       varchar(100) not null,
  tel       char(10)
) ENGINE InnoDB;

CREATE TABLE livres (
  NL        integer primary key auto_increment,
  editeur   varchar(50),
  NO        integer not null, 
  foreign key(NO) references oeuvres(NO)
) ENGINE InnoDB;

CREATE TABLE categories(
  NC        integer primary key auto_increment,
  categorie varchar(150)
) ENGINE InnoDB;

CREATE TABLE thematique (
  NO        integer not null,
  NC        integer not null, 
  foreign key(NO) references oeuvres(NO),
  foreign key(NC) references categories(NC),
  primary key (NO, NC)
) ENGINE InnoDB;

CREATE TABLE emprunter (
  NL        integer not null,
  datEmp    date not null,
  dureeMax  integer not null,
  dateRet   date,
  NA        integer not null, 
  foreign key(NA) references adherents(NA),
  foreign key(NL) references livres(NL),
  primary key (NL, datEmp)
) ENGINE InnoDB;

INSERT INTO oeuvres VALUES 
(1,'Narcisse et Goldmund','Hermann HESSE'),
(2,'Berenice','Jean RACINE'),
(3,'Prolégomènes à  toute métaphysique future','Emmanuel KANT'),
(4,'Mon coeur mis à nu','Charles BAUDELAIRE'),
(5,'Voyage au bout de la nuit','Louis-Ferdinand CELINE'),
(6,'Les possédés','Fedor DOSTOIEVSKI'),
(7,'Le Rouge et le Noir','STENDHAL'),
(8,'Alcibiade','Jacqueline de ROMILLY'),
(9,'Monsieur Teste','Paul VALERY'),
(10,'Lettres de Gourgounel','Kenneth WHITE'),
(11,'Lettres à un jeune poète','Rainer Maria RILKE'),
(12,'Logique sans peine','Lewis CAROLL'),
(13,'L''éthique','Baruch SPINOZA'),
(14,'Sur le rêve','Sigmund FREUD'),
(15,'Sens et dénotation','Gottlob FREGE'),
(16,'Penser la logique','Gilbert HOTTOIS'),
(17,'Au coeur des ténèbres','Joseph CONRAD'),
(18, 'Mathématiques pour l''informatique - BTS SIO', 'Xavier CHANET et Patrick VERT'),
(19, 'Méthodes mathématiques pour l''informatique', 'Jacques VELU'),
(20, 'Notions de logiques', 'Philippe THIRY'),
(21, 'Eléments de logique contemporaine', 'François LEPAGE'),
(22, 'Histoire d''algorithmes', 'Jean-Luc CHABERT'),
(23, 'Harry Potter, I : Harry Potter à l''école des sorciers', 'Joanne Kathleen ROWLING'),
(24, 'Harry Potter, II : Harry Potter et la Chambre des Secrets', 'Joanne Kathleen ROWLING'),
(25, 'Harry Potter, III : Harry Potter et le prisonnier d''Azkaban', 'Joanne Kathleen ROWLING'),
(26, 'Harry Potter, IV : Harry Potter et la Coupe de Feu', 'Joanne Kathleen ROWLING'),
(27, 'Harry Potter, V : Harry Potter et l''Ordre du Phénix', 'Joanne Kathleen ROWLING'),
(28, 'Harry Potter, VI : Harry Potter et le Prince de Sang-Mêlé', 'Joanne Kathleen ROWLING'),
(29, 'Harry Potter, VII : Harry Potter et les Reliques de la Mort', 'Joanne Kathleen ROWLING'),
(30, 'Oliver Twist', 'Charles DICKENS'),
(31, 'David Copperfield', 'Charles DICKENS'),
(32, 'Le Combat d''hiver', 'Jean-Claude MOURLEVAT'),
(33, 'Terrienne', 'Jean-Claude MOURLEVAT'),
(34, 'La Montagne magique','Thomas MANN'),
(35, 'A la recherche du temps perdu, I : Du côté de chez Swann', 'Marcel PROUST');


INSERT INTO livres VALUES 
(1,  'GF',         1), #(1,'Narcisse et Goldmund','Hermann HESSE'),
(2,  'FOLIO',      2), #
(3,  'HACHETTE',   3), #
(4,  'GF',         4), #
(5,  'FOLIO',      5), #
(6,  'FOLIO',      6), #
(7,  'GF',         7), #
(8,  'FOLIO',      8), #
(9,  'HACHETTE',   9), #
(10, 'GF',        10), #
(11, 'HACHETTE',  11), #
(12, 'FOLIO',     12), #
(13, 'GF',        13), #
(14, 'FOLIO',     14), #
(15, 'HACHETTE',  15), #
(16, 'HACHETTE',  16), #
(17, 'FOLIO',      1), #(1,'Narcisse et Goldmund','Hermann HESSE'),
(18, 'FOLIO',      2), #
(19, 'HACHETTE',   2), #
(20, 'FOLIO',      4), #
(21, 'GF',         5), #
(22, 'HACHETTE',   4), #
(23, 'HACHETTE',   7), #
(24, 'FOLIO',      8), #
(25, 'GF',         1), #(1,'Narcisse et Goldmund','Hermann HESSE'),
(26, 'HACHETTE',  10), #
(27, 'FOLIO',     11), #
(28, 'FOLIO',     12), #
(29, 'GF',         1), #(1,'Narcisse et Goldmund','Hermann HESSE'),
(30, 'HACHETTE',  14), #
(31, 'FOLIO',     17), #
(32, 'DUNOD',     18), #
(33, 'DUNOD',     19), #
(34, 'DE BOECK',  20), #(20, 'Notions de logiques', 'Philippe THIRY'),
(35, 'DUNOD',     21), #(21, 'Eléments de logique contemporaine', 'François LEPAGE'),
(36, 'BELIN',     22), #(22, 'Histoire d''algorithmes', 'Jean-Luc CHABERT'),
(37, 'FOLIO',     23), #(23, 'Harry Potter, I : Harry Potter à l''école des sorciers', 'Joanne Kathleen ROWLING'),
(38, 'FOLIO',     24), #(24, 'Harry Potter, II : Harry Potter et la Chambre des Secrets', 'Joanne Kathleen ROWLING'),
(39, 'FOLIO',     25), #(25, 'Harry Potter, III : Harry Potter et le prisonnier d''Azkaban', 'Joanne Kathleen ROWLING'),
(40, 'FOLIO',     26), #(26, 'Harry Potter, IV : Harry Potter et la Coupe de Feu', 'Joanne Kathleen ROWLING'),
(41, 'FOLIO',     27), #(27, 'Harry Potter, V : Harry Potter et l''Ordre du Phénix', 'Joanne Kathleen ROWLING'),
(42, 'FOLIO',     28), #(28, 'Harry Potter, VI : Harry Potter et le Prince de Sang-Mêlé', 'Joanne Kathleen ROWLING'),
(43, 'FOLIO',     29), #(29, 'Harry Potter, VII : Harry Potter et les Reliques de la Mort', 'Joanne Kathleen ROWLING'),
(44, 'HACHETTE',  30), #(30, 'Oliver Twist', 'Charles DICKENS'),
(45, 'HACHETTE',  31), #(31, 'David Copperfield', 'Charles DICKENS'),
(46, 'FOLIO',     23), #(23, 'Harry Potter, I : Harry Potter à l''école des sorciers', 'Joanne Kathleen ROWLING'),
(47, 'GALLIMARD', 32), #(32, 'Le Combat d''hiver', 'Jean-Claude MOURLEVAT'),
(48, 'GALLIMARD', 33), #(33, 'Terrienne', 'Jean-Claude MOURLEVAT'),
(49, 'FOLIO',     34), #(34, 'La Montagne magique','Thomas MANN'),
(50, 'FOLIO',     35); #(35, 'A la recherche du temps perdu, I : Du côté de chez Swann', 'Marcel PROUST');

INSERT INTO categories VALUES
(1, 'Roman'),
(2, 'Jeunesse'),
(3, 'Theatre'),
(4, 'Poesie'),
(5, 'Mathematiques'),
(6, 'Sorciers'),
(7, 'Informatique'),
(8, 'Logique'),
(9, 'philosophie'),
(10, 'sciences'),
(11, 'roman étranger'),
(12, 'psychologie');

INSERT INTO thematique VALUES
(1,   1),
(1,  11), 
(2,   3), 
(3,   9),
(3,  10), 
(4,   4), 
(5,   1), 
(6,   1), 
(6,  11), 
(7,   1), 
(8,   1), 
(9,   1),
(9,   9),
(10,  4), 
(11,  4),
(12,  8),
(13,  9),
(14,  12),
(14,  10),
(15,   9),
(15,   8),
(16,   8),
(16,   9),
(17,   1),
(17,  11),
(18,   5),
(18,   7),
(19,   5),
(19,   7),
(20,   8),
(21,   8),
(22,   8),
(22,   7),
(22,   5),
(23,   1),
(23,  11),
(23,   2),
(23,   6),
(24,   1),
(24,  11),
(24,   2),
(24,   6),
(25,   1),
(25,  11),
(25,   2),
(25,   6),
(26,   1),
(26,  11),
(26,   2),
(26,   6),
(27,   1),
(27,  11),
(27,   2),
(27,   6),
(28,   1),
(28,  11),
(28,   2),
(28,   6),
(29,   1),
(29,  11),
(29,   2),
(29,   6),
(30,   1),
(30,  11),
(31,   1),
(31,  11),
(32,   1),
(32,   2),
(32,   6),
(33,   1),
(33,   2),
(34,   1),
(34,  11),
(35,   1);

INSERT INTO adherents VALUES 
(1,'Lecoeur','Jeanette','16 rue de la République, 75010 Paris','0145279274'),
(2,'Lecoeur','Philippe','16 rue de la République, 75010 Paris','0145279274'),
(3,'Dupont','Yvan','73 rue Lamarck, 75018 Paris','0163538294'),
(4,'Mercier','Claude','155 avenue Parmentier, 75011 Paris','0136482736'),
(5,'Léger','Marc','90 avenue du Maine, 75014 Paris','0164832947'),
(6,'Martin','Laure','51 boulevard Diderot, 75012 Paris','0174693277'),
(7,'Crozier','Martine','88 rue des Portes Blanches, 75018 Paris','0146829384'),
(8,'Lebon','Clément','196 boulevard de Sebastopol, 75001 Paris','0132884739'),
(9,'Dufour','Jacques','32 rue des Alouettes, 75003 Paris','0155382940'),
(10,'Dufour','Antoine','32 rue des Alouettes, 75003 Paris','0155382940'),
(11,'Dufour','Stéphanie','32 rue des Alouettes, 75003 Paris','0155382940'),
(12,'Raymond','Carole','35 rue Oberkampf, 75011 Paris','0153829402'),
(13,'Durand','Albert','4 rue Mandar, 75002 Paris','0642374021'),
(14,'Wilson','Paul','12 rue Paul Vaillant Couturier, 92400 Montrouge','0642327407'),
(15,'Grecault','Philippe','15 rue de la Roquette, 75012 Paris','0132762983'),
(16,'Carre','Stéphane','51 boulevard Diderot, 75012 Paris','0174693277'),
(17,'Johnson','Astrid','3 rue Léon Blum, 75002 Paris','0143762947'),
(18,'Mirou','Caroline','2 square Mirabeau, 75011 Paris','0163827399'),
(19,'Espelette','Jean-Jacques','141 avenue de France, 75019 Paris','0134887264'),
(20,'Despentes','Anthony','56 boulevard de la Villette, 75019 Paris','0133889463'),
(21,'Terlu','Véronique','45 rue des Batignolles, 75020 Paris','0165998372'),
(22,'Rihour','Cécile','7 rue Montorgueil, 75002 Paris','0166894754'),
(23,'Franchet','Pierre','160 rue Montmartre, 75009 Paris','0633628549'),
(24,'Trochet','Ernest','34 rue de l''Esperance, 75008 Paris','0638295563'),
(25,'Gainard','Simon','55 rue Desnouettes, 75015 Paris','0174928934'),
(26,'Touche','Johanna','14 rue du Bac, 75006 Paris','0619384065'),
(27,'Cornu','Sylvain','22 rue Mouffetard, 75005 Paris','0184927489'),
(28,'Frederic','Cyril','15 rue du Simplon, 75018 Paris','0173625492'),
(29,'Crestard','Cedric','5 rue Doudeauville, 75018 Paris','0629485700'),
(30,'Le Bihan','Karine','170 bis rue Ordener, 75018 Paris','0638995221'),
(31,'Dos Santos','Olivia','58 rue Montmartre, 75009 Paris','0634353049'),
(32,'Cheurfa','Nour', '21 rue de Paradis, 75010 Paris','0130304512'),
(33,'Tanrhori','Mustafa', '17 rue du Chateau d''eau, 75010 Paris','0930404510');


INSERT INTO emprunter 
(NL, datemp,                               dureeMax, dateRet,                               NA) VALUES 
(1,  from_days(to_days(current_date)-350), 21,       from_days(to_days(current_date)-349),  26),
(4,  from_days(to_days(current_date)-323), 21,       from_days(to_days(current_date)-310),   4),
(26, from_days(to_days(current_date)-315), 21,       from_days(to_days(current_date)-318),   9),
(25, from_days(to_days(current_date)-311), 21,       from_days(to_days(current_date)-293),   1),
(12, from_days(to_days(current_date)-300), 21,       from_days(to_days(current_date)-1290),  7),
(20, from_days(to_days(current_date)-283), 21,       from_days(to_days(current_date)-282),  27),
(37, from_days(to_days(current_date)-280), 14,       from_days(to_days(current_date)-275),   1),
(10, from_days(to_days(current_date)-273), 21,       from_days(to_days(current_date)-250),   7),
(4,  from_days(to_days(current_date)-232), 14,       from_days(to_days(current_date)-228),  12),
(24, from_days(to_days(current_date)-226), 14,       from_days(to_days(current_date)-220),  26),
(38, from_days(to_days(current_date)-226), 14,       from_days(to_days(current_date)-200),   2),
(8,  from_days(to_days(current_date)-201), 14,       from_days(to_days(current_date)-183),  13),
(6,  from_days(to_days(current_date)-199), 14,       from_days(to_days(current_date)-194),   3),
(10, from_days(to_days(current_date)-169), 14,       from_days(to_days(current_date)-157),   8),
(1,  from_days(to_days(current_date)-153), 14,       from_days(to_days(current_date)-142),   3),
(15, from_days(to_days(current_date)-146), 14,       from_days(to_days(current_date)-138),  10),
(1,  from_days(to_days(current_date)-106), 14,       from_days(to_days(current_date)-101),   2),
(4,  from_days(to_days(current_date)-103), 14,       from_days(to_days(current_date)-93),    5),
(37, from_days(to_days(current_date)-100), 14,       from_days(to_days(current_date)-90),    1),
(38, from_days(to_days(current_date)-100), 14,       from_days(to_days(current_date)-90),    1),
(18, from_days(to_days(current_date)-86),  14,       from_days(to_days(current_date)-79),    3),
(8,  from_days(to_days(current_date)-76),  14,       from_days(to_days(current_date)-70),   18),
(2,  from_days(to_days(current_date)-37),  14,       from_days(to_days(current_date)-28),    4),
(1,  from_days(to_days(current_date)-28),  14,       from_days(to_days(current_date)-23),    1),
(3,  from_days(to_days(current_date)-21),  14,       from_days(to_days(current_date)-17),    3),
(20, from_days(to_days(current_date)-24),  14,       from_days(to_days(current_date)-8),     9),
(21, from_days(to_days(current_date)-23),  14,       from_days(to_days(current_date)-11),   14),
(1,  from_days(to_days(current_date)-10),  14,       NULL,                                  28),
(2,  from_days(to_days(current_date)-10),  14,       NULL,                                  28),
(9,  from_days(to_days(current_date)-10),  14,       NULL,                                  28),
(14, from_days(to_days(current_date)-9),   14,       NULL,                                   1),
(16, from_days(to_days(current_date)-9),   14,       NULL,                                   1),
(5,  from_days(to_days(current_date)-5),   14,       NULL,                                  16),
(28, from_days(to_days(current_date)-10),  14,       NULL,                                  16),
(29, from_days(to_days(current_date)-395), 14,       NULL,                                  27),
(11, from_days(to_days(current_date)-30),  14,       NULL,                                  22),
(3 , from_days(to_days(current_date)-30),  14,       NULL,                                  22),
(31, from_days(to_days(current_date)-1),   14,       NULL,                                  20),
(21, from_days(to_days(current_date)-1),   14,       NULL,                                  20),
(38, from_days(to_days(current_date)-3),   14,       NULL,                                  31),
(39, from_days(to_days(current_date)-3),   14,       NULL,                                  31),
(40, from_days(to_days(current_date)-3),   14,       NULL,                                  31),
(10, from_days(to_days(current_date)-25),  14,       NULL,                                  33),
(18, from_days(to_days(current_date)-20),  14,       NULL,                                  33),
(19, from_days(to_days(current_date)-20),  14,       NULL,                                  33);

