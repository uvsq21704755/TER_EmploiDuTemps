CREATE table Seance
(
	NumSeance Int PRIMARY KEY NOT NULL,
	Jour Varchar(50),
	HeureDebut Varchar(5),
	HeureFin Varchar(5),
	IdEnseignant int,
	NomSalle varchar(50)
	FOREIGN KEY(IdEnseignant) REFERENCES Enseignant(num_ens)
	FOREIGN KEY(NomSalle) REFERENCES Salle(NomSalle)
);

INSERT INTO Seance VALUES(1, 'Mardi', '9h40', '12h50', 85045461, 'Amphi E');
INSERT INTO Seance VALUES(2, 'Mercredi', '9h40', '12h50', 85028604, 'Amphi E');
INSERT INTO Seance VALUES(3, 'Vendredi', '9h40', '12h50', 73710800, 'Amphi E');
INSERT INTO Seance VALUES(4, 'Mardi', '13h50', '18h40', 85045461, 'G105');
INSERT INTO Seance VALUES(5, 'Mercredi', '13h50', '18h40', 85045461, 'G105');
INSERT INTO Seance VALUES(6, 'Mercredi', '13h50', '18h40', 85028604, 'JUNGLE');
INSERT INTO Seance VALUES(7, 'Jeudi', '9h40', '12h50', 81951043, 'Amphi H');
INSERT INTO Seance VALUES(8, 'Jeudi', '13h50', '18h40', 73710800, 'JUNGLE');
INSERT INTO Seance VALUES(9, 'Jeudi', '13h50', '18h40', 81951043, 'G203');
INSERT INTO Seance VALUES(10, 'Jeudi', '13h50', '18h40', 39047430, 'G204');
INSERT INTO Seance VALUES(11, 'Vendredi', '13h50', '18h40', 85028604, 'ALSACE');
INSERT INTO Seance VALUES(12, 'Vendredi', '13h50', '18h40', 73710800, 'RC22');
