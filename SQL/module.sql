-- Création de la table Enseignant --

CREATE TABLE Module
(
    Code VARCHAR(10) PRIMARY KEY NOT NULL,
    Intitule VARCHAR(100),
    Groupe INT
);

-- Insertion des tuples --

INSERT INTO module(Code, Intitule) VALUES ('MIN17214','Conception de BD');
INSERT INTO module(Code, Intitule) VALUES ('MIN17211','Methodes de Ranking');
INSERT INTO module(Code, Intitule) VALUES ('MIN17217','Application Web et Securite');
INSERT INTO module(Code, Intitule) VALUES ('MIN17213','Tuning de BD');
INSERT INTO module(Code, Intitule) VALUES ('MIN17215','Protocoles IP');
INSERT INTO module(Code, Intitule) VALUES ('MIN17218','Calcul Securise');
INSERT INTO module(Code, Intitule) VALUES ('MIN17212','Simulation');
INSERT INTO module(Code, Intitule) VALUES ('MIN17216','Reseaux etendus');
