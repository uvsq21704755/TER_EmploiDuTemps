
-- Création de la table Enseignant --

CREATE TABLE Creneau
(
	IdCreneau INT PRIMARY KEY NOT NULL,
	Jour Varchar(10),
	HeureDebut Varchar(5),
  HeureFin Varchar(5)
);

-- Insertion des tuples --

INSERT INTO Creneau VALUES (1, 'Lundi', '9h40', '12h50');
INSERT INTO Creneau VALUES (2, 'Mardi', '9h40', '12h50');
INSERT INTO Creneau VALUES (3, 'Mercredi', '9h40', '12h50');
INSERT INTO Creneau VALUES (4, 'Jeudi', '9h40', '12h50');
INSERT INTO Creneau VALUES (5, 'Vendredi', '9h40', '12h50');
INSERT INTO Creneau VALUES (6, 'Lundi', '13h50', '18h40');
INSERT INTO Creneau VALUES (7, 'Mardi', '13h50', '18h40');
INSERT INTO Creneau VALUES (8, 'Mercredi', '13h50', '18h40');
INSERT INTO Creneau VALUES (9, 'Jeudi', '13h50', '18h40');
INSERT INTO Creneau VALUES (10, 'Vendredi', '13h50', '18h40');
INSERT INTO Creneau VALUES (11, 'Lundi', '8h00', '12h50');
INSERT INTO Creneau VALUES (12, 'Mardi', '8h00', '12h50');
INSERT INTO Creneau VALUES (13, 'Mercredi', '8h00', '12h50');
INSERT INTO Creneau VALUES (14, 'Jeudi', '8h00', '12h50');
INSERT INTO Creneau VALUES (15, 'Vendredi', '8h00', '12h50');
