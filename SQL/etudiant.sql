

-- Création de la base de données --

CREATE DATABASE Universite;



-- Création de la table Etudiant --

CREATE table Etudiant
(
	NumEtudiant Int PRIMARY KEY NOT NULL,
	Nom Varchar(30),
	Prénom Varchar(30),
	Formation Varchar(30)
);



-- Insertion des tuples --

INSERT INTO Etudiant VALUES('21704755', 'Sugumar', 'Thivagini', 'M1 DATASCALE');
INSERT INTO Etudiant VALUES('22106935', 'Varenne-Paquet', 'Julie', 'M1 DATASCALE');
INSERT INTO Etudiant VALUES('22208420', 'Ahmed', 'Moulhat', 'M1 DATASCALE');
INSERT INTO Etudiant VALUES('21506184','Raymond','Julien','M1 SECRETS');
INSERT INTO Etudiant VALUES('21508783','Lecoq','Camille','M1 AMIS');
INSERT INTO Etudiant VALUES('21504311','Begue','Patricia','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21501801','Besnard','Adrien','M1 SECRETS');
INSERT INTO Etudiant VALUES('21503511','Gosselin','Amélie','M1 SECRETS');
INSERT INTO Etudiant VALUES('21507042','Lebrun','Aurore','M1 AMIS');
INSERT INTO Etudiant VALUES('21500056','Lebon','Camille','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21603046','Nicolas','Adrien','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21603909','Deschamps','Nathalie','M1 SECRETS');
INSERT INTO Etudiant VALUES('21609592','Pineau','Amélie','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21608275','Rodrigues','Luc','M1 SECRETS');
INSERT INTO Etudiant VALUES('21605935','Legrand','Martin','M1 AMIS');
INSERT INTO Etudiant VALUES('21607130','Coulon','Lucie','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21604216','Vincent','Victor','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21701935','Marchand','Thomas','M1 AMIS');
INSERT INTO Etudiant VALUES('21707481','Bertin','Paul','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21709456','Duhamel','Martin','M1 SECRETS');
INSERT INTO Etudiant VALUES('21700097','Coste','Laurent','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21700992','Loiseau','Sylvie','M1 AMIS');
INSERT INTO Etudiant VALUES('21703897','Laporte','Paul','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21703347','Delaunay','Alain','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21702843','Legros','Xavier','M1 SECRETS');
INSERT INTO Etudiant VALUES('21705376','Delattre','Eléonore','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21701255','Boulay','Clément','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21709716','Albert','Claire','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21709918','Carlier','Emilie','M1 AMIS');
INSERT INTO Etudiant VALUES('21701894','Chevalier','Philippe','M1 SECRETS');
INSERT INTO Etudiant VALUES('21702183','Perret','Suzanne','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21703113','Courtois','Océane','M1 AMIS');
INSERT INTO Etudiant VALUES('21800735','Marin','Gabriel','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21800448','Levy','','M1 AMIS');
INSERT INTO Etudiant VALUES('21801326','Bertrand','Martin','M1 SECRETS');
INSERT INTO Etudiant VALUES('21809906','Tessier','Louise','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21806921','Dufour','Alice','M1 SECRETS');
INSERT INTO Etudiant VALUES('21805436','Berthelot','Marine','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21809246','Lemoine','Mathilde','M1 AMIS');
INSERT INTO Etudiant VALUES('21807240','Peron','Alexandre','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21804369','Delorme','Marie','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21807557','Costa','Quentin','M1 SECRETS');
INSERT INTO Etudiant VALUES('21801240','Gilles','Maxime','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21809269','Hubert','Zoé','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21803338','Lefevre','Tristan','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21800364','Brun','Kévin','M1 AMIS');
INSERT INTO Etudiant VALUES('21806340','Lagarde','Arnaud','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21804053','Germain','Arthur','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21803288','Leroux','Sabine','M1 SECRETS');
INSERT INTO Etudiant VALUES('21804977','Roche','Antoine','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21800330','Dubois','Valentin','M1 SECRETS');
INSERT INTO Etudiant VALUES('21800371','Roussel','Robert','M1 AMIS');
INSERT INTO Etudiant VALUES('21803710','Lecomte','Laurène','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21800324','Perrot','','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21802446','Charpentier','Thibault','M1 SECRETS');
INSERT INTO Etudiant VALUES('21804717','Valette','Philippine','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21806229','Fouquet','Stéphanie','M1 AMIS');
INSERT INTO Etudiant VALUES('21800102','Leroy','Mélissa','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21802809','Guillot','Louis','M1 SECRETS');
INSERT INTO Etudiant VALUES('21804194','Pichon','Léa','M1 AMIS');
INSERT INTO Etudiant VALUES('21805575','Masse','Lola','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21805143','Reynaud','Lucas','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21802843','Goncalves','Margot','M1 AMIS');
INSERT INTO Etudiant VALUES('21805063','Brun','Juliette','M1 SECRETS');
INSERT INTO Etudiant VALUES('21808685','Odette','Alfred','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21800989','Gillet','Elodie','M1 AMIS');
INSERT INTO Etudiant VALUES('21807527','Garnier','Thérèse','M1 SECRETS');
INSERT INTO Etudiant VALUES('21809974','Olivier','Laurence','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21809975','Bouvet','Hélène','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21809776','Payet','Valentine','M1 SECRETS');
INSERT INTO Etudiant VALUES('21808097','Vidal','Clémence','M1 AMIS');
INSERT INTO Etudiant VALUES('21800184','Cohen','Maëlle','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21805277','Michaud','Flora','M1 SECRETS');
INSERT INTO Etudiant VALUES('21805656','Potier','Fiona','M1 AMIS');
INSERT INTO Etudiant VALUES('21805208','Aubert','Astrid','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21802726','Weber','Chloé','M1 AMIS');
INSERT INTO Etudiant VALUES('21802798','Bailly','Luhanne','M1 SECRETS');
INSERT INTO Etudiant VALUES('21801552','Guyon','Jeanne','M1 SECRETS');
INSERT INTO Etudiant VALUES('21908786','Henry','Lucie','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21903954','Lebreton','Jade','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21909784','Huet','Diane','M1 AMIS');
INSERT INTO Etudiant VALUES('21902684','Bruneau','Donia','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21909223','Lemonnier','Pauline','M1 SECRETS');
INSERT INTO Etudiant VALUES('21902464','Fournier','Benjamin','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21906007','Allard','Célia','M1 AMIS');
INSERT INTO Etudiant VALUES('21901767','Turpin','Laure','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21907525','Martinez','Georges','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21904321','Marty','Jean','M1 DATASCALE');
INSERT INTO Etudiant VALUES('21904624','Joubert','Benoît','M1 RESEAUX');
INSERT INTO Etudiant VALUES('21905169','Dumas','Susan','M1 SECRETS');
INSERT INTO Etudiant VALUES('21907812','Meyer','Julia','M1 AMIS');
INSERT INTO Etudiant VALUES('21909975','Jacquet','Léo','M1 SECRETS');
INSERT INTO Etudiant VALUES('21905199','Roy','Pierre','M1 AMIS');
INSERT INTO Etudiant VALUES('21905792','Baron','Théo','M1 AMIS');
INSERT INTO Etudiant VALUES('21903380','Blanchet','Théophile','M1 SECRETS');
INSERT INTO Etudiant VALUES('22005674','Gallet','Tanguy','M1 RESEAUX');
INSERT INTO Etudiant VALUES('22002951','Rey','Charles','M1 DATASCALE');
INSERT INTO Etudiant VALUES('22003891','Carre','Franck','M1 RESEAUX');
INSERT INTO Etudiant VALUES('22002492','Robin','Marianne','M1 SECRETS');
INSERT INTO Etudiant VALUES('22007883','Boulanger','Jules','M1 AMIS');
INSERT INTO Etudiant VALUES('22005574','Moreno','Mathilda','M1 AMIS');
INSERT INTO Etudiant VALUES('22001332','Gomez','Virginie','M1 DATASCALE');
INSERT INTO Etudiant VALUES('22000522','Ledoux','Marion','M1 AMIS');
INSERT INTO Etudiant VALUES('22006388','Ramos','Emma','M1 RESEAUX');
INSERT INTO Etudiant VALUES('22004021','Petit','Elise','M1 DATASCALE');
INSERT INTO Etudiant VALUES('22103125','Blanchard','Mathieu','M1 RESEAUX');
INSERT INTO Etudiant VALUES('22107121','Bouchet','Enzo','M1 SECRETS');
INSERT INTO Etudiant VALUES('22108321','Lenoir','Antoine','M1 AMIS');
INSERT INTO Etudiant VALUES('22107235','Pelletier','Yann','M1 AMIS');
INSERT INTO Etudiant VALUES('22102659','Verdier','Baptiste','M1 DATASCALE');
INSERT INTO Etudiant VALUES('22102970','Samson','Hugo','M1 SECRETS');
INSERT INTO Etudiant VALUES('22102638','Regnier','Marco','M1 DATASCALE');
INSERT INTO Etudiant VALUES('22102228','Girard','Laetitia','M1 AMIS');
INSERT INTO Etudiant VALUES('22100524','Becker','Aurélie','M1 RESEAUX');
INSERT INTO Etudiant VALUES('22106489','Menard','Thierry','M1 SECRETS');
INSERT INTO Etudiant VALUES('22105336','Becker','Capucine','M1 DATASCALE');
INSERT INTO Etudiant VALUES('22105689','Ruiz','Clothilde','M1 AMIS');
INSERT INTO Etudiant VALUES('22100358','Schneider','Anaïs','M1 AMIS');
INSERT INTO Etudiant VALUES('22102358','Blanc','Grégoire','M1 DATASCALE');
INSERT INTO Etudiant VALUES('22102443','Ferreira','Filipe','M1 SECRETS');
