DROP TABLE IF EXISTS Enseignant;
CREATE TABLE IF NOT EXISTS Enseignant(
	num_ens serial primary key,
	nom varchar(100) not null,
	prenom varchar(100) not null
);

insert into Enseignant(nom,prenom) values  
	('Payet', 'Jeanne'),
    ('Lecomte', 'Lou'),
    ('Dupuy', 'Aghate'),
    ('Guillot', 'Romane'),
    ('Deschamps', 'Chamila'),
    ('Jacquet', 'Mélanie'),
    ('Shneidier', 'Elodie'),
    ('Collet', 'Leonie'),
    ('Leger', 'Adele'),
    ('Bouviet', 'Iris'),
	('Cully', 'Georgette'),
	('Huguenin', 'Gisleine'),
	('Hautmonte', 'Noel'),
	('Demange', 'Noelle'),
	('Bellecourt', 'Michelle'),
	('Poireau', 'Luc'),
	('Fremiau', 'Denis'),
	('Febve', 'Charlie'),
	('Salmon', 'Bernard'),
	('Verdonk', 'Henry'),
	('Fringuant', 'Philippe'),
	('Tintingere', 'Mike'),
    ('Valentin', 'Bob'),
    ('Mougel', 'Marc'),
    ('Rublond', 'Billy'),
    ('Martin', 'Dalya'),
    ('Vauthier', 'Eric'),
    ('Smith', 'Kevin'),
    ('Andre', 'Christian'),
    ('Villemain', 'Andre');

