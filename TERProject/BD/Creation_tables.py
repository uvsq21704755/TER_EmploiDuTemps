from BD.Connexion import (connexion,close_connexion)
import psycopg2


def create_tables():
    try:
        conn = connexion()
        cur = conn.cursor()
        sql = open("script.sql","r").read()
        cur.execute(sql)
        conn.commit()
        print("Création des tables réalisée avec succès")

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la création des tables", error)

def delete_all():
    try:
        conn = connexion()
        cur = conn.cursor()
        sql = "truncate table contient,Optionsf,enseigne,inscrit, seance, salle, creneau, enseignant, etudiant,  matiere, formation;"
        cur.execute(sql)
        conn.commit()
        print("Suppressions avec succès")
        close_connexion(conn,cur)
    except (Exception, psycopg2.Error) as error:
        print("Erreur lors des suppressions dans les tables", error)


