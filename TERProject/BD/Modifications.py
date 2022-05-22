from TERProject.BD.Connexion import (connexion,close_connexion)
import psycopg2
from TERProject.Models.Creneau import Creneau
from TERProject.Models.Salle import Salle
from TERProject.Models.Enseignant import Enseignant
from TERProject.Models.Etudiant import Etudiant
from TERProject.Models.Formation import Formation
from TERProject.Models.Matiere import Matiere
from TERProject.Models.Seance import Seance
from TERProject.Models.Groupe import Groupe

def modif_student_inscription(idStudent,groupe,module):
    try:
        conn = connexion()
        cur = conn.cursor()
        sql = "SELECT Code FROM Matiere where Code  = (%s) "
        cur.execute(sql,(module,))
        res = cur.fetchall()
        for tuple in res:
            for r in tuple:
                result = r
        sql1 ="UPDATE Inscrit SET Groupe  = {} where NumEtudiant = {} and CodeModule = (%s) "
        cur.execute(sql1.format(groupe,idStudent),(r,))
        conn.commit()
        count = cur.rowcount
        close_connexion(conn, cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la mise à jour du groupe", error)
def supp_student_inscription(idStudent,module):
    try:
        conn = connexion()
        cur = conn.cursor()
        sql = "SELECT Code FROM Matiere where Code  = (%s) "
        cur.execute(sql,(module,))
        res = cur.fetchall()
        for tuple in res:
            for r in tuple:
                result = r
        sql1 ="DELETE FROM Inscrit where NumEtudiant = {} and CodeModule = (%s) "
        cur.execute(sql1.format(idStudent),(r,))
        conn.commit()
        count = cur.rowcount
        close_connexion(conn, cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la mise à jour du groupe", error)
def modif_seance(numseance,idcreneau):
    try:
        conn = connexion()
        cur = conn.cursor()
        sql1 ="UPDATE Seance SET IdCreneau  = {} where NumSeance = (%s)  "
        cur.execute(sql1.format(idcreneau),(numseance,))
        conn.commit()
        count = cur.rowcount
        close_connexion(conn, cur)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la mise à jour du groupe", error)
