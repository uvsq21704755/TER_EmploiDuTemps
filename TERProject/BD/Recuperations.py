from BD.Connexion import (connexion,close_connexion)
import psycopg2
from Models.Creneau import Creneau
from Models.Salle import Salle
from Models.Enseignant import Enseignant
from Models.Etudiant import Etudiant
from Models.Formation import Formation
from Models.Matiere import Matiere
from Models.Seance import Seance
from Models.Groupe import Groupe

def all_students():
    try:
        mesetudiants = []
        conn = connexion()
        cur = conn.cursor()
        sql = "SELECT * FROM Etudiant"
        sql2 = "SELECT count(*) FROM Etudiant"
        sql3 = "SELECT e.numEtudiant, m.Intitule from Etudiant e, Matiere m, inscrit i WHERE e.NumEtudiant = i.NumEtudiant AND m.Code = i.CodeModule"
        print("Select des étudiants")
        cur.execute(sql)
        res = cur.fetchall()
        print("Stockage des étudiants dans une liste")
        cur.execute(sql3)
        res3 = cur.fetchall()
        for tuple in res:
            sesmatieres  = []
            for tuple3 in res3:
                if tuple3[0] == tuple[0]:
                    sesmatieres.append(tuple3[1])
            etudiant = Etudiant(tuple[0],tuple[1],tuple[2],tuple[3],sesmatieres)
            mesetudiants.append(etudiant)
        print("Récupération des etudiants réalisée avec succès")
        cur.execute(sql2)
        res2 = cur.fetchall()
        for tuple2 in res2:
            print("Il y'a ", tuple2[0], "étudiants")
        close_connexion(conn,cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la création des tables", error)

    #for etudiant in mesetudiants:
    #    etudiant.affichage()
    return mesetudiants
def all_instructor():
    try:
        mesenseignants = []
        conn = connexion()
        cur = conn.cursor()
        sql = "SELECT * FROM Enseignant"
        sql2 = "SELECT count(*) FROM Enseignant"
        sql3 = "SELECT e.IdEnseignant, m.Intitule from Enseignant e, Matiere m, enseigne i WHERE e.IdEnseignant = i.IdEnseignant AND m.Code = i.CodeModule"
        print("Select des enseignants")
        cur.execute(sql)
        res = cur.fetchall()
        print("Stockage des enseignants dans une liste")
        cur.execute(sql3)
        res3 = cur.fetchall()
        for tuple in res:
            sesmatieres  = []
            for tuple3 in res3:
                if tuple3[0] == tuple[0]:
                    sesmatieres.append(tuple3[1])
            enseignant = Enseignant(tuple[0],tuple[1],tuple[2],sesmatieres)
            mesenseignants.append(enseignant)
        print("Récupération des enseignants réalisée avec succès")
        cur.execute(sql2)
        res2 = cur.fetchall()
        for tuple2 in res2:
            print("Il y'a ", tuple2[0], "enseignants")
        close_connexion(conn,cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la création des tables", error)

    #for enseignant in mesenseignants:
    #    enseignant.afficher()
    return mesenseignants
def all_formations():
    try:
        mesformations = []
        conn = connexion()
        cur = conn.cursor()
        sql = "SELECT * FROM Formation"
        sql2 = "SELECT count(*) FROM Formation"
        sql3 = "SELECT f.Intitule, m.Intitule from Formation f, Matiere m, contient c WHERE f.Intitule = c.IntituleFormation AND m.Code = c.CodeModule"
        sql4 = "SELECT f.Intitule, m.Intitule from Formation f, Matiere m, optionsf o WHERE f.Intitule = o.IntituleFormation AND m.Code = o.CodeModule"

        print("Select des formations")
        cur.execute(sql)
        res = cur.fetchall()
        print("Stockage des formations dans une liste")
        cur.execute(sql3)
        res3 = cur.fetchall()
        cur.execute(sql4)
        res4 = cur.fetchall()
        for tuple in res:
            sesmatieres = []
            sesoptions = []
            for tuple3 in res3:
                if tuple3[0] == tuple[0]:
                    sesmatieres.append(tuple3[1])
            for tuple4 in res4:
                if tuple4[0] == tuple[0]:
                    sesoptions.append(tuple4[1])
            formation = Formation(tuple[0], tuple[1], sesmatieres, sesoptions)
            mesformations.append(formation)
        print("Récupération des formations réalisée avec succès")
        cur.execute(sql2)
        res2 = cur.fetchall()
        for tuple2 in res2:
            print("Il y'a ", tuple2[0], "formations")
        close_connexion(conn, cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la création des tables", error)

    # for formation in mesformations:
    #    formation.affichage()
    return mesformations
def all_modules():
    try:
        mesmatieres = []
        conn = connexion()
        cur = conn.cursor()
        sql = "SELECT * FROM Matiere"
        sql2 = "SELECT count(*) FROM Matiere"
        print("Select des modules")
        cur.execute(sql)
        res = cur.fetchall()
        print("Stockage des modules dans une liste")
        for tuple in res:
            matiere = Matiere(tuple[0], tuple[1],tuple[2])
            mesmatieres.append(matiere)
        print("Récupération des matieres réalisée avec succès")
        cur.execute(sql2)
        res2 = cur.fetchall()
        for tuple2 in res2:
            print("Il y'a ", tuple2[0], "matieres")
        close_connexion(conn, cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la création des tables", error)

    # for matiere in mesmatieres:
    #    matiere.affichage()
    return mesmatieres
def all_creneaux():
    try:
        mescreneaux = []
        conn = connexion()
        cur = conn.cursor()
        sql = "SELECT * FROM Creneau"
        sql2 = "SELECT count(*) FROM Creneau"
        print("Select des creneaux")
        cur.execute(sql)
        res = cur.fetchall()
        print("Stockage des creneaux dans une liste")
        for tuple in res:
            hdeb = tuple[2].split("h")
            heuredeb = hdeb[0] + "." + hdeb[1]
            heuredebut = float(heuredeb)
            hfin = tuple[3].split("h")
            heurefin = hfin[0] + "." + hfin[1]
            heurefin = float(heurefin)
            creneau = Creneau(tuple[0], tuple[1],heuredebut,heurefin)
            mescreneaux.append(creneau)
        print("Récupération des creneaux réalisée avec succès")
        cur.execute(sql2)
        res2 = cur.fetchall()
        for tuple2 in res2:
            print("Il y'a ", tuple2[0], "créneaux")
        close_connexion(conn, cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la création des tables", error)

    #for creneau in mescreneaux:
    #    creneau.affichage()
    return mescreneaux
def all_rooms():
    try:
        messalles = []
        conn = connexion()
        cur = conn.cursor()
        sql = "SELECT * FROM Salle"
        sql2 = "SELECT count(*) FROM Salle"
        print("Select des salles")
        cur.execute(sql)
        res = cur.fetchall()
        print("Stockage des salles dans une liste")
        for tuple in res:
            salle = Salle(tuple[0], tuple[1],tuple[2])
            messalles.append(salle)
        print("Récupération des salles réalisée avec succès")
        cur.execute(sql2)
        res2 = cur.fetchall()
        for tuple2 in res2:
            print("Il y'a ", tuple2[0], "salles")
        close_connexion(conn, cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la création des tables", error)

    #for salle in messalles:
    #    salle.affichage()
    return messalles
def all_seances():
    try:
        messeances = []
        conn = connexion()
        cur = conn.cursor()
        sql = "SELECT s.NumSeance,c.Jour, c.HeureDebut, c.HeureFin, s.NomSalle , e.Nom, s.NumGroupe, m.Intitule FROM Seance s, Salle, Matiere m, Enseignant e, Creneau c WHERE s.NomSalle = Salle.NomSalle AND m.Code = s.CodeModule AND e.IdEnseignant = s.IdEnseignant AND c.IdCreneau = s.IdCreneau "
        sql2 = "SELECT count(*) FROM Seance"
        print("Select des seances")
        cur.execute(sql)
        res = cur.fetchall()
        print("Stockage des seances dans une liste")
        for tuple in res:
            hdeb = tuple[2].split("h")
            heuredeb = hdeb[0] + "." + hdeb[1]
            heuredebut = float(heuredeb)
            hfin = tuple[3].split("h")
            heurefin = hfin[0] + "." + hfin[1]
            heurefin = float(heurefin)
            seance = Seance(tuple[0],tuple[1],heuredebut,heurefin,tuple[4],tuple[5],tuple[6],tuple[7])
            messeances.append(seance)
        print("Récupération des seances réalisée avec succès")
        cur.execute(sql2)
        res2 = cur.fetchall()
        for tuple2 in res2:
            print("Il y'a ", tuple2[0], "seances")
        close_connexion(conn, cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la création des tables", error)

    #for seance in messeances:
    #    seance.affichage()
    return messeances
