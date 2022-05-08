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
from BD.Creation_tables import (create_tables,delete_all)
from BD.Insertions import insertions_bd
from BD.Recuperations import (all_students,all_instructor,all_formations,all_modules, all_creneaux, all_rooms, all_seances)
from BD.Modifications import modif_student_inscription

listeModules = all_modules()
listeFormations = all_formations()

def combi_interdits():
    liste = []
    for module in listeModules:
        for module2 in listeModules:
            if module.get_code() != module2.get_code():
                for module3 in listeModules:
                    if (module3.get_code() != module2.get_code()) and (module3.get_code() != module.get_code()):
                        for module4 in listeModules:
                            if module4.get_code() != module3.get_code() and module4.get_code() != module2.get_code() and module4.get_code() != module.get_code():
                                listeadd = []
                                listeadd.extend([module.get_intitule(),module2.get_intitule(),module3.get_intitule(),module4.get_intitule()])
                                listeadd.sort()
                                if listeadd not in liste:
                                    liste.append(listeadd)
    print(liste)
    print(len(liste))

#def liste_combinaisons():
combi_interdits()
