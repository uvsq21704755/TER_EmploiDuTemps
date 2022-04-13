DROP TABLE IF EXISTS Enseignant;
CREATE TABLE IF NOT EXISTS Enseignant(
	num_ens serial primary key,
	nom varchar(100) not null,
	prenom varchar(100) not null
);

insert into Enseignant values  
	(81951043,'Payet', 'Jeanne'),
	(73710800,'Lecomte', 'Lou'),
	(39047430'Dupuy', 'Aghate'),
	(85045461,'Guillot', 'Romane'),
	(85028604,'Deschamps', 'Chamila'),
	(85553092,'Jacquet', 'Mélanie'),
	(24752580,'Shneidier', 'Elodie'),
	(90162770,'Collet', 'Leonie'),
	(32621692,'Leger', 'Adele'),
	(82669712,'Bouviet', 'Iris'),
	(23823539,'Cully', 'Georgette'),
	(98162030,'Huguenin', 'Gisleine'),
	(10730719,'Hautmonte', 'Noel'),
	(65144866,'Demange', 'Noelle'),
	(18411108,'Bellecourt', 'Michelle'),
	(73898507,'Poireau', 'Luc'),
	(37102506,'Fremiau', 'Denis'),
	(66407015,'Febve', 'Charlie'),
	(12607024,'Salmon', 'Bernard'),
	(90372061,'Verdonk', 'Henry'),
	(41518102,'Fringuant', 'Philippe'),
	(74409814,'Tintingere', 'Mike'),
	(55134490,'Valentin', 'Bob'),
	(93610981,'Mougel', 'Marc'),
	(89245974,'Rublond', 'Billy'),
	(18107116,'Martin', 'Dalya'),
	(41754373,'Vauthier', 'Eric'),
	(57276663,'Smith', 'Kevin'),
	(84446076'Andre', 'Christian'),
	(78130198'Villemain', 'Andre');

