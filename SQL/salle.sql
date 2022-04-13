CREATE table Salle
(
	NomSalle varchar(50) PRIMARY KEY NOT NULL,
	Type Varchar(30),
	Capacite int
);

INSERT INTO Salle VALUES('G105', 'Cours', 30);
INSERT INTO Salle VALUES('G205', 'Informatique', 30);
