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

def modif_student_inscription(idStudent,groupe,intitule_module):
    try:
        conn = connexion()
        cur = conn.cursor()
        print("Update groupe étudiant")
        sql = "SELECT Code FROM Matiere where Intitule  = (%s) "
        cur.execute(sql,(intitule_module,))
        res = cur.fetchall()
        for tuple in res:
            for r in tuple:
                result = r
        sql1 ="UPDATE Inscrit SET Groupe  = {} where NumEtudiant = {} and CodeModule = (%s) "
        cur.execute(sql1.format(groupe,idStudent),(r,))
        conn.commit()
        count = cur.rowcount
        print(count,"Groupe d'un étudiant mis à jour avec succès dans la table Inscrit")
        close_connexion(conn, cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la mise à jour du tuple", error)