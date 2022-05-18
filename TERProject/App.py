from BD.Creation_tables import (create_tables,delete_all)
from BD.Insertions import insertions_bd
from BD.Recuperations import (all_students,all_instructor,all_formations,all_modules, all_creneaux, all_rooms, all_seances, matiere_nb_groupe, matiere_nb_eleves, verif_affectation,seances_etudiant_p1,return_groupe_etudiant)
from BD.Modifications import modif_student_inscription
from Algorithme.Donnees import (liste_combinaisons_p1,liste_combinaisons_p2,affectation_combi_etudiant_p1,creation_groupe_p1,affectation_etudiants_groupe_p1,conflits1, calcul_conflits, algo)
if __name__ == '__main__':

    delete_all()
    create_tables()
    algo()

