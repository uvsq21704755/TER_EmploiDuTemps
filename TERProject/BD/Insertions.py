from Models.Creneau import Creneau
from Models.Salle import Salle
from Models.Enseignant import Enseignant
from Models.Etudiant import Etudiant
from Models.Formation import Formation
from Models.Matiere import Matiere
from Models.Seance import Seance
from Models.Groupe import Groupe
import psycopg2
from BD.Connexion import (connexion, close_connexion)


def insertions_bd():
    insert_formations()
    insert_etudiant_inscrit()
    insert_matieres()
    insert_enseignant_enseigne()
    insert_creneaux()
    insert_salles()
    # insert_seances()
def insert_groupes(listegroupes):
    try:
        conn = connexion()
        cur = conn.cursor()
        sql = """INSERT INTO Groupe(NumGroupe, CodeModule, NbEleves) VALUES (%s,%s,%s)"""
        for groupe in listegroupes:
            value = (groupe.get_numero(), groupe.get_matiere(), groupe.get_nbeleves())
            cur.execute(sql, value)
            conn.commit()
            count = cur.rowcount
        close_connexion(conn, cur)
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors des insertions dans les tables", error)
def insert_matieres():
    mesmatieres = []
    fin = 0;
    while fin != 1:
        print("Créez votre nouvelle matiere :")
        code = input("Precisez le code : ")
        intitule = input("Précisez l'intitule : ")
        nbGroupes = int(input("Précisez le nombre de Groupes : "))

        matieres = Matiere(code,intitule,nbGroupes)
        mesmatieres.append(matieres)
        question = input("Voulez-vous encore rajouter une matiere ? Répondez par oui ou non : ")
        if (question == "non"):
            fin = 1
        else:
            fin = 0

    try:
        conn = connexion()
        cur = conn.cursor()
        sql = """INSERT INTO Matiere(Code,Intitule,Groupes) VALUES (%s,%s,%s);"""
        for matiere in mesmatieres:
            value = (matiere.get_code(),matiere.get_intitule(),matiere.get_nbGroupes())
            cur.execute(sql,value)
            conn.commit()
            count = cur.rowcount
            print(count, "enregistrement inséré avec succès dans la table matiere.")
        close_connexion(conn, cur)
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors des insertions dans les tables", error)
def insert_formations():
    mesformations = []
    fin = 0;
    while fin != 1:
        print("Créez votre nouvelle formation :")
        nom = input("Précisez le nom : ")
        code = input("Precisez le code : ")
        listematiere = input(
            "Précisez la liste des matieres qu'elle propose dans la forme matiere1,matiere2,MAtiere3 ... : ").split(",")
        options = input(
            "Précisez la liste des options qu'elle propose dans la forme matiere1,matiere2,MAtiere3 ... : ").split(",")
        formations = Formation(nom,code,listematiere,options)
        mesformations.append(formations)
        question = input("Voulez-vous encore rajouter une formation ? Répondez par oui ou non : ")
        if (question == "non"):
            fin = 1
        else:
            fin = 0

    try:
        conn = connexion()
        cur = conn.cursor()
        sql = """INSERT INTO formation(Intitule,Code) VALUES (%s,%s);"""
        for formation in mesformations:
            value = (formation.get_nom(),formation.get_code())
            cur.execute(sql,value)
            conn.commit()
            count = cur.rowcount
            print(count, "enregistrement inséré avec succès dans la table formation.")
        close_connexion(conn, cur)
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors des insertions dans les tables", error)
def insert_etudiant_inscrit():
    mesetudiants = []
    fin = 0;
    while fin != 1:
        print("Créez votre nouvel etudiant :")
        numetudiant = int(input(" Quel est le numero de votre etudiant : "))
        nom = input("Précisez le nom : ")
        prenom = input("Précisez le prenom : ")
        formation = input("Dans quel formation est inscrit cet étudiant : ")
        liste1 = input(
            "Précisez la liste des matieres dans lesquelles il est inscrit dans la forme matiere1,matiere2,MAtiere3 ... : ").split(",")
        liste2 = input(
            "Précisez la liste des matieres dans lesquelles il est inscrit dans la forme matiere1,matiere2,MAtiere3 ... : ").split(
            ",")
        etudiants = Etudiant(numetudiant, nom, prenom, formation,liste1,liste2)
        mesetudiants.append(etudiants)
        question = input("Voulez-vous encore rajouter un etudiant ? Répondez par oui ou non : ")
        if (question == "non"):
            fin = 1
        else:
            fin = 0

    try:
        conn = connexion()
        cur = conn.cursor()
        sql = """INSERT INTO Etudiant(NumEtudiant, Nom, Prenom, Formation) VALUES (%s,%s,%s,%s)"""
        for etudiant in mesetudiants:
            liste = []
            liste.append(etudiant.get_matieres_s1())
            liste.append(etudiant.get_matieres_s2())
            value = (etudiant.get_numetudiant(), etudiant.get_nom(), etudiant.get_prenom(), etudiant.get_formation())
            cur.execute(sql, value)
            conn.commit()
            count = cur.rowcount
            print(count, "enregistrement inséré avec succès dans la table etudiant.")
        close_connexion(conn, cur)
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors des insertions dans les tables", error)

def insert_creneaux():
    mescreneaux = []
    fin = 0;
    while fin != 1:
        print("Créez votre nouveau créneau :")
        id = int(input(" Quel est l'id de votre créneau : "))
        jour = input("Précisez le jour : ")
        hdeb = input("Précisez l'heure de début : ")
        hfin = input("Précisez l'heure de fin  : ")
        creneau = Creneau(id, jour, hdeb, hfin)
        mescreneaux.append(creneau)
        question = input("Voulez-vous encore rajouter un créneau ? Répondez par oui ou non : ")
        if (question == "non"):
            fin = 1
        else:
            fin = 0

    try:
        conn = connexion()
        cur = conn.cursor()
        sql = """INSERT INTO creneau(IdCreneau, Jour, Heuredebut, Heurefin) VALUES (%s,%s,%s,%s)"""
        for creneau in mescreneaux:
            value = (creneau.get_id(), creneau.get_jour(), creneau.get_hdeb(), creneau.get_hfin())
            cur.execute(sql, value)
            conn.commit()
            count = cur.rowcount
            print(count, "enregistrement inséré avec succès dans la table creneau.")
        close_connexion(conn, cur)
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors des insertions dans les tables", error)
def insert_salles():
    mesSalles = []
    fin = 0;
    while fin != 1:
        print("Créez votre nouvelle salle :")
        nom = input(" Quel est le nom de votre salle : ")
        type_salle = input("Précisez le type de la salle : ")
        capacite = int(input("Quelle est la capacité d'accueil de votre salle : "))

        salles = Salle(nom,type_salle,capacite)
        mesSalles.append(salles)
        question = input("Voulez-vous encore rajouter une autre salle ? Répondez par oui ou non : ")
        if (question == "non"):
            fin = 1
        else:
            fin = 0

    try:
        conn = connexion()
        cur = conn.cursor()
        sql = """INSERT INTO salle(NomSalle, Type, Capacite) VALUES (%s,%s,%s)"""
        for salle in mesSalles:
            value = (salle.get_nom(),salle.get_typesalle(),salle.get_capacite())
            cur.execute(sql, value)
            conn.commit()
            count = cur.rowcount
            print(count, "enregistrement inséré avec succès dans la table salle.")
        close_connexion(conn, cur)
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors des insertions dans les tables", error)
def insert_enseignant_enseigne():
    mesenseignants = []
    fin = 0;
    while fin != 1:
        print("Créez votre nouvel enseignant :")
        id = int(input(" Quel est l'id de votre enseignant : "))
        nom = input("Précisez le nom : ")
        prenom = input("Précisez le prenom : ")
        listematiere = input("Précisez la liste des matieres qu'il enseigne dans la forme matiere1,matiere2,MAtiere3 ... : ").split(",")
        enseignants = Enseignant(id, nom, prenom, listematiere)
        mesenseignants.append(enseignants)
        question = input("Voulez-vous encore rajouter un enseignant ? Répondez par oui ou non : ")
        if (question == "non"):
            fin = 1
        else:
            fin = 0

    try:
        conn = connexion()
        cur = conn.cursor()
        sql = """INSERT INTO enseignant(IdEnseignant, Nom, Prenom) VALUES (%s,%s,%s)"""
        for enseignant in mesenseignants:
            value = (enseignant.get_id(), enseignant.get_nom(), enseignant.get_prenom())
            cur.execute(sql, value)
            conn.commit()
            count = cur.rowcount
            print(count, "enregistrement inséré avec succès dans la table enseignant.")
        close_connexion(conn, cur)
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors des insertions dans les tables", error)