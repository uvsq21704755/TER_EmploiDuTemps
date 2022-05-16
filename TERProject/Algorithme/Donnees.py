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
from BD.Recuperations import (all_students,all_instructor,all_formations,all_modules, all_creneaux, all_rooms, all_seances,matiere_nb_groupe,matiere_nb_eleves, verif_affectation, seances_etudiant)
from BD.Modifications import modif_student_inscription


def liste_combinaisons_s1():
    listeEtudiants = all_students()

    liste = []
    for etudiant in listeEtudiants:
        combi = []
        for matiere in etudiant.get_matieres_s1():
            combi.append(matiere)
        combi.sort()
        if combi not in liste:
            liste.append(combi)

    return liste
def liste_combinaisons_s2():
    listeEtudiants = all_students()

    liste = []
    for etudiant in listeEtudiants:
        combi = []
        for matiere in etudiant.get_matieres_s2():
            combi.append(matiere)
        combi.sort()
        if combi not in liste:
            liste.append(combi)

    return liste
def affectation_combi_etudiant_s1():
    combinaisons = liste_combinaisons_s1()
    etudiants = all_students()
    affectation = []
    for combi in combinaisons:
        item = []
        item.append(combi)
        for etudiant in etudiants:
            combi_etudiant = []
            for combi2 in etudiant.get_matieres_s1():
                combi_etudiant.append(combi2)
            combi_etudiant.sort()
            if combi_etudiant == combi:
                item.append(etudiant.get_numetudiant())
        affectation.append(item)

    return affectation
def affectation_combi_etudiant_s2():
    combinaisons = liste_combinaisons_s2()
    etudiants = all_students()
    affectation = []
    for combi in combinaisons:
        item = []
        item.append(combi)
        for etudiant in etudiants:
            combi_etudiant = []
            for combi2 in etudiant.get_matieres_s2():
                combi_etudiant.append(combi2)
            combi_etudiant.sort()
            if combi_etudiant == combi:
                item.append(etudiant.get_numetudiant())
        affectation.append(item)

    return affectation
def creation_groupe():
    matieres = all_modules()
    groupes = []
    for matiere in matieres:
        nb_grpe = matiere.get_nbGroupes()
        nb_grpe_tmp = nb_grpe
        nb_eleves = matiere_nb_eleves(matiere.get_intitule())
        nb_eleves_tmp = nb_eleves
        nb_eleves_grpe = nb_eleves_tmp // nb_grpe_tmp

        # création des groupes pour chaque matiere (sans la liste des eleves)
        for item in range(1,nb_grpe+1):
            nb_eleves_tmp = nb_eleves_tmp - nb_eleves_grpe
            if nb_eleves_tmp == 1:
                nb_eleves_grpe = nb_eleves_grpe + 1
            groupe = Groupe(matiere.get_intitule(),item,nb_eleves_grpe)
            groupes.append(groupe)
    return groupes
def affectation_etudiants_groupe_s1():
    groupes = creation_groupe()
    affects = affectation_combi_etudiant_s1()
    for groupe in groupes:
        liste_etudiants = []
        nb_eleves_tmp = groupe.get_nbeleves()
        for affect in affects:
            for matiere in affect[0]:
                if matiere == groupe.get_matiere():
                    for etudiant in affect:
                        if etudiant != affect[0]  and etudiant not in liste_etudiants and nb_eleves_tmp > 0 and verif_affectation(matiere,etudiant) == False:
                            liste_etudiants.append(etudiant)
                            nb_eleves_tmp = nb_eleves_tmp - 1
                            modif_student_inscription(etudiant,groupe.get_numero(),matiere)
        groupe.set_liste_eleves(liste_etudiants)

    return groupes
def affectation_etudiants_groupe_s2():
    groupes = creation_groupe()
    affects = affectation_combi_etudiant_s2()
    for groupe in groupes:
        liste_etudiants = []
        nb_eleves_tmp = groupe.get_nbeleves()
        for affect in affects:
            for matiere in affect[0]:
                if matiere == groupe.get_matiere():
                    for etudiant in affect:
                        if etudiant != affect[0]  and etudiant not in liste_etudiants and nb_eleves_tmp > 0 and verif_affectation(matiere,etudiant) == False:
                            liste_etudiants.append(etudiant)
                            nb_eleves_tmp = nb_eleves_tmp - 1
                            modif_student_inscription(etudiant,groupe.get_numero(),matiere)
        groupe.set_liste_eleves(liste_etudiants)

    return groupes
def conflits():
    etudiants = all_students()
    liste_conflits = []
    for etudiant in etudiants:
        item = []
        conflit = 0
        seances = seances_etudiant(etudiant.get_numetudiant())
        for seance1 in seances:
            for seance2 in seances:
                if seance1 != seance2:
                    if seance1[1] == seance2[1]:
                        hdeb1 = seance1[2].split("h")
                        heuredeb1 = hdeb1[0] + "." + hdeb1[1]
                        heuredebut1 = float(heuredeb1)
                        hdeb2 = seance2[2].split("h")
                        heuredeb2 = hdeb2[0] + "." + hdeb2[1]
                        heuredebut2 = float(heuredeb2)

                        hfin1 = seance1[3].split("h")
                        hrefin1 = hfin1[0] + "." + hfin1[1]
                        heurefin1 = float(hrefin1)
                        hfin2 = seance2[2].split("h")
                        hrefin2 = hfin2[0] + "." + hfin2[1]
                        heurefin2 = float(hrefin2)

                        if heuredebut1 == heuredebut2:
                            conflit = conflit + 1
                        elif heuredebut1 == heurefin2:
                            conflit = conflit + 1
                        elif heuredebut2 == heurefin1:
                            conflit = conflit + 1
                        elif heurefin1 == heurefin2:
                            conflit = conflit + 1
                        elif heuredebut2 > heuredebut1 and heuredebut2 <= heurefin1:
                            conflit = conflit + 1
                        elif heuredebut2 < heuredebut1 and heurefin2 >= heuredebut1:
                            conflit = conflit + 1
        if conflit > 0:
            item.append(etudiant.get_numetudiant())
            item.append(conflit)
            liste_conflits.append(item)
    return liste_conflits

def calcul_conflits(liste_conflits):
    result = 0
    for conflit in liste_conflits:
            result = result + conflit[1]
    return result


