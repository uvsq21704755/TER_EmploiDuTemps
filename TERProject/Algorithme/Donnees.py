
from BD.Connexion import (connexion,close_connexion)
import random
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
from BD.Insertions import (insertions_bd,insert_groupes)
from BD.Recuperations import (all_students,all_instructor,all_formations,all_modules, all_modules_p1, all_modules_p2, all_creneaux, all_rooms, all_seances,matiere_nb_groupe,matiere_nb_eleves, verif_affectation, seances_etudiant_p1, seances_etudiant_p2, return_groupe_etudiant, etudiants_in_module)
from BD.Modifications import modif_student_inscription


def liste_combinaisons_p1():
    listeEtudiants = all_students()

    liste = []
    for etudiant in listeEtudiants:
        combi = []
        for matiere in etudiant.get_matieres_p1():
            combi.append(matiere)
        combi.sort()
        if combi not in liste:
            liste.append(combi)

    return liste
def liste_combinaisons_p2():
    listeEtudiants = all_students()

    liste = []
    for etudiant in listeEtudiants:
        combi = []
        for matiere in etudiant.get_matieres_p2():
            combi.append(matiere)
        combi.sort()
        if combi not in liste:
            liste.append(combi)

    return liste
def affectation_combi_etudiant_p1():
    combinaisons = liste_combinaisons_p1()
    etudiants = all_students()
    affectation = []
    for combi in combinaisons:
        item = []
        item.append(combi)
        for etudiant in etudiants:
            combi_etudiant = []
            for combi2 in etudiant.get_matieres_p1():
                combi_etudiant.append(combi2)
            combi_etudiant.sort()
            if combi_etudiant == combi:
                item.append(etudiant.get_numetudiant())
        affectation.append(item)

    return affectation
def affectation_combi_etudiant_p2():
    combinaisons = liste_combinaisons_p2()
    etudiants = all_students()
    affectation = []
    for combi in combinaisons:
        item = []
        item.append(combi)
        for etudiant in etudiants:
            combi_etudiant = []
            for combi2 in etudiant.get_matieres_p2():
                combi_etudiant.append(combi2)
            combi_etudiant.sort()
            if combi_etudiant == combi:
                item.append(etudiant.get_numetudiant())
        affectation.append(item)

    return affectation
def creation_groupe_p1():
    matieres = all_modules_p1()
    groupes = []
    for matiere in matieres:
        nb_grpe = matiere.get_nbGroupes()
        nb_eleves = matiere_nb_eleves(matiere.get_code())
        nb_eleves_grpe = nb_eleves//nb_grpe

        # création des groupes pour chaque matiere (sans la liste des eleves)
        for item in range(1,nb_grpe+1):
            nb_eleves = nb_eleves - nb_eleves_grpe
            if nb_eleves == 1:
                nb_eleves_grpe = nb_eleves_grpe + 1
            groupe = Groupe(matiere.get_code(),item,nb_eleves_grpe)
            groupes.append(groupe)
    insert_groupes(groupes)
    return groupes
def creation_groupe_p2():
    matieres = all_modules_p2()
    groupes = []
    for matiere in matieres:
        nb_grpe = matiere.get_nbGroupes()
        nb_eleves = matiere_nb_eleves(matiere.get_code())
        nb_eleves_grpe = nb_eleves//nb_grpe

        # création des groupes pour chaque matiere (sans la liste des eleves)
        for item in range(1,nb_grpe+1):
            nb_eleves = nb_eleves - nb_eleves_grpe
            if nb_eleves == 1:
                nb_eleves_grpe = nb_eleves_grpe + 1
            groupe = Groupe(matiere.get_code(),item,nb_eleves_grpe)
            groupes.append(groupe)
    insert_groupes(groupes)
    return groupes
def affectation_etudiants_groupe_p1():
    groupes = creation_groupe_p1()
    affects = affectation_combi_etudiant_p1()
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
def affectation_etudiants_groupe_p2():
    groupes = creation_groupe_p2()
    affects = affectation_combi_etudiant_p2()
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
def affectation_etudiants_groupe_aleatoire_p1():
    groupes = creation_groupe_p1()
    for groupe in groupes:
        tmp = groupe.get_nbeleves()
        liste = etudiants_in_module(groupe.get_matiere())
        eleves = []
        while tmp > 0:
            etudiant = random.randint(0,len(liste)-1)
            if liste[etudiant] not in eleves and verif_affectation(groupe.get_matiere(),etudiant) == False:
                eleves.append(liste[etudiant])
                tmp -= 1
                modif_student_inscription(liste[etudiant], groupe.get_numero(), groupe.get_matiere())
        groupe.set_liste_eleves(eleves)
    return groupes
def conflits1():
    etudiants = all_students()
    liste_conflits = []
    for etudiant in etudiants:
        item = []
        conflit = 0
        seances = seances_etudiant_p1(etudiant.get_numetudiant())
        for seance1 in seances:
            for seance2 in seances:
                if seance1 != seance2:
                    if seance1[1] == seance2[1]:
                        item2 = []
                        item2.append(seance1[0])
                        item2.append(seance2[0])
                        item2.sort()
                        if item2 not in item:
                            item.append(item2)
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
                        else:
                            item.remove(item2)

        if conflit > 0:
            item.append(etudiant.get_numetudiant())
            item.append(conflit)
            liste_conflits.append(item)
    result = 0

    for conflit5 in liste_conflits:
        add = conflit5[len(conflit5) - 1]
        cpt = len(conflit5) - 2
        if cpt < add:
            add = cpt
            conflit5[len(conflit5) - 1] = add
    return liste_conflits

def conflits2():
    etudiants = all_students()
    liste_conflits = []
    for etudiant in etudiants:
        item = []
        conflit = 0
        seances = seances_etudiant_p2(etudiant.get_numetudiant())
        for seance1 in seances:
            for seance2 in seances:
                if seance1 != seance2:
                    if seance1[1] == seance2[1]:
                        item2 = []
                        item2.append(seance1[0])
                        item2.append(seance2[0])
                        item2.sort()
                        if item2 not in item:
                            item.append(item2)
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
                        else:
                            item.remove(item2)

        if conflit > 0:
            item.append(etudiant.get_numetudiant())
            item.append(conflit)
            liste_conflits.append(item)
    result = 0

    for conflit5 in liste_conflits:
        add = conflit5[len(conflit5) - 1]
        cpt = len(conflit5) - 2
        if cpt < add:
            add = cpt
            conflit5[len(conflit5) - 1] = add
    return liste_conflits

def calcul_conflits(liste_conflits):
    result = 0
    #for conflit in liste_conflits:
    #    result = result + conflit[len(conflit)-1]
    result = len(liste_conflits)
    return result

def algo1():
    groupes_initiale = affectation_etudiants_groupe_p1()
    liste_conflits = conflits1()
    conflit = calcul_conflits(liste_conflits)
    print("La solution initiale a {} conflits".format(conflit))
    #groupes_initiale_tmp = groupes_initiale
    memorise_conflits = []
    memorise_groupe = []
    memorise_groupe.append(groupes_initiale)
    memorise_conflits.append(conflit)

    groupes_deja_vu1 = []
    for groupe in groupes_initiale:
        if matiere_nb_groupe(groupe.get_matiere()) == 1:
            continue
        for groupe2 in groupes_initiale:
            if groupe != groupe2 and groupe.get_matiere() == groupe2.get_matiere() and groupe2 not in groupes_deja_vu1:
                min = groupe.get_nbeleves()
                if groupe2.get_nbeleves() < min:
                    min = groupe2.get_nbeleves()
                liste_grpe1 = []
                liste_grpe2 = []
                for etudiant1 in groupe.get_liste_eleves():
                    liste_grpe1.append(etudiant1)
                for etudiant2 in groupe2.get_liste_eleves():
                    liste_grpe2.append(etudiant2)
                for i in range(0,min-1):
                    tmp = liste_grpe1[i]
                    liste_grpe1[i] = liste_grpe2[i]
                    modif_student_inscription(liste_grpe1[i], groupe.get_numero(), groupe.get_matiere())
                    liste_grpe2[i] = tmp
                    modif_student_inscription(liste_grpe2[i], groupe2.get_numero(), groupe.get_matiere())
                index = groupes_initiale.index(groupe)
                index2 = groupes_initiale.index(groupe2)
                groupe.set_liste_eleves(liste_grpe1)
                groupe2.set_liste_eleves(liste_grpe2)
                groupes_initiale[index] = groupe
                groupes_initiale[index2] = groupe2
                groupes_deja_vu1.append(groupe)
                groupes_deja_vu1.append(groupe2)
    liste_conflits2 = conflits1()
    conflit2 = calcul_conflits(liste_conflits2)
    print("Pic amélioration : {} conflits".format(conflit2))
    memorise_groupe.append(groupes_initiale)
    memorise_conflits.append(conflit2)



    cpt = 0

    for iteration in range(10):
        if cpt > 5:
            break
        groupes_deja_vu = []
        for groupe in groupes_initiale:
            if matiere_nb_groupe(groupe.get_matiere()) == 1:
                continue
            for groupe2 in groupes_initiale:
                if groupe != groupe2 and groupe.get_matiere() == groupe2.get_matiere() and groupe2 not in groupes_deja_vu:
                    liste1 = []
                    liste2 = []
                    liste_grpe1 = []
                    liste_grpe2 = []
                    for etudiant1 in groupe.get_liste_eleves():
                        liste_grpe1.append(etudiant1)
                    for etudiant2 in groupe2.get_liste_eleves():
                        liste_grpe2.append(etudiant2)

                    for i in range(12):
                        n1 = random.randint(0, len(liste_grpe1)-1)
                        n2 = random.randint(0, len(liste_grpe2)-1)
                        while liste_grpe1[n1] in liste1:
                            n1 = random.randint(0, 20)
                        while liste_grpe2[n2] in liste2:
                            n2 = random.randint(0, 20)
                        eleve1 = liste_grpe1[n1]
                        eleve2 = liste_grpe2[n2]
                        liste1.append(eleve1)
                        liste_grpe1.remove(eleve1)
                        liste2.append(eleve2)
                        liste_grpe2.remove(eleve2)
                    for eleve in liste1:
                        liste_grpe2.append(eleve)
                        modif_student_inscription(eleve, groupe2.get_numero(), groupe2.get_matiere())
                    for etudiant in liste2:
                        liste_grpe1.append(etudiant)
                        modif_student_inscription(etudiant, groupe.get_numero(), groupe.get_matiere())
                    index = groupes_initiale.index(groupe)
                    index2 = groupes_initiale.index(groupe2)
                    groupe.set_liste_eleves(liste_grpe1)
                    groupe2.set_liste_eleves(liste_grpe2)
                    groupes_initiale[index] = groupe
                    groupes_initiale[index2] = groupe2
                    #groupes_deja_vu.append(groupe)

                    liste_conflits_new1 = conflits1()
                    conflit_new1 = calcul_conflits(liste_conflits_new1)

                    if (conflit_new1 < memorise_conflits[len(memorise_conflits) - 1]):
                        print("Amélioration. Le nouveau conflit est : ", conflit_new1)
                        memorise_groupe.append(groupes_initiale)
                        memorise_conflits.append(conflit_new1)
                    else:
                        print(" Pas d'amélioration avec ce groupe")
                        cpt += 1
                        groupes_initiale = memorise_groupe[len(memorise_groupe) - 1]
                        for groupe in groupes_initiale:
                            for eleve5 in groupe.get_liste_eleves():
                                modif_student_inscription(eleve5, groupe.get_numero(), groupe.get_matiere())


        liste_conflits_new = conflits1()
        conflit_new = calcul_conflits(liste_conflits_new)

        if(conflit_new < memorise_conflits[len(memorise_conflits)-1]):
            print("Amélioration. Le nouveau conflit est : ", conflit_new)
            memorise_groupe.append(groupes_initiale)
            memorise_conflits.append(conflit_new)
        else:
            print(" pas d'amélioration")
            cpt += 20
            groupes_initiale = memorise_groupe[len(memorise_groupe)-1]
            for groupe in groupes_initiale:
                for eleve5 in groupe.get_liste_eleves():
                    modif_student_inscription(eleve5, groupe.get_numero(), groupe.get_matiere())
    print("Fin des iterations")

    result = []
    result.append(memorise_groupe[0])
    result.append(memorise_conflits[0])
    result.append((memorise_groupe[1]))
    result.append(memorise_conflits[1])
    result.append(memorise_groupe[len(memorise_groupe)-1])
    result.append(memorise_conflits[len(memorise_conflits)-1])

    return result
def algo2():
    groupes_initiale = affectation_etudiants_groupe_p2()
    liste_conflits = conflits2()
    conflit = calcul_conflits(liste_conflits)
    print("La solution initiale a {} conflits".format(conflit))
    #groupes_initiale_tmp = groupes_initiale
    memorise_conflits = []
    memorise_groupe = []
    memorise_groupe.append(groupes_initiale)
    memorise_conflits.append(conflit)

    groupes_deja_vu1 = []
    for groupe in groupes_initiale:
        if matiere_nb_groupe(groupe.get_matiere()) == 1:
            continue
        for groupe2 in groupes_initiale:
            if groupe != groupe2 and groupe.get_matiere() == groupe2.get_matiere() and groupe2 not in groupes_deja_vu1:
                min = groupe.get_nbeleves()
                if groupe2.get_nbeleves() < min:
                    min = groupe2.get_nbeleves()
                liste_grpe1 = []
                liste_grpe2 = []
                for etudiant1 in groupe.get_liste_eleves():
                    liste_grpe1.append(etudiant1)
                for etudiant2 in groupe2.get_liste_eleves():
                    liste_grpe2.append(etudiant2)
                for i in range(0,min-1):
                    tmp = liste_grpe1[i]
                    liste_grpe1[i] = liste_grpe2[i]
                    modif_student_inscription(liste_grpe1[i], groupe.get_numero(), groupe.get_matiere())
                    liste_grpe2[i] = tmp
                    modif_student_inscription(liste_grpe2[i], groupe2.get_numero(), groupe.get_matiere())
                index = groupes_initiale.index(groupe)
                index2 = groupes_initiale.index(groupe2)
                groupe.set_liste_eleves(liste_grpe1)
                groupe2.set_liste_eleves(liste_grpe2)
                groupes_initiale[index] = groupe
                groupes_initiale[index2] = groupe2
                groupes_deja_vu1.append(groupe)
                groupes_deja_vu1.append(groupe2)
    liste_conflits2 = conflits2()
    conflit22 = calcul_conflits(liste_conflits2)
    print("Pic amélioration : {} conflits".format(conflit22))
    memorise_groupe.append(groupes_initiale)
    memorise_conflits.append(conflit22)



    cpt = 0

    for iteration in range(10):
        if cpt > 5:
            break
        groupes_deja_vu = []
        for groupe in groupes_initiale:
            if matiere_nb_groupe(groupe.get_matiere()) == 1:
                continue
            for groupe2 in groupes_initiale:
                if groupe != groupe2 and groupe.get_matiere() == groupe2.get_matiere() and groupe2 not in groupes_deja_vu:
                    liste1 = []
                    liste2 = []
                    liste_grpe1 = []
                    liste_grpe2 = []
                    for etudiant1 in groupe.get_liste_eleves():
                        liste_grpe1.append(etudiant1)
                    for etudiant2 in groupe2.get_liste_eleves():
                        liste_grpe2.append(etudiant2)

                    for i in range(12):
                        n1 = random.randint(0, len(liste_grpe1)-1)
                        n2 = random.randint(0, len(liste_grpe2)-1)
                        while liste_grpe1[n1] in liste1:
                            n1 = random.randint(0, 20)
                        while liste_grpe2[n2] in liste2:
                            n2 = random.randint(0, 20)
                        eleve1 = liste_grpe1[n1]
                        eleve2 = liste_grpe2[n2]
                        liste1.append(eleve1)
                        liste_grpe1.remove(eleve1)
                        liste2.append(eleve2)
                        liste_grpe2.remove(eleve2)
                    for eleve in liste1:
                        liste_grpe2.append(eleve)
                        modif_student_inscription(eleve, groupe2.get_numero(), groupe2.get_matiere())
                    for etudiant in liste2:
                        liste_grpe1.append(etudiant)
                        modif_student_inscription(etudiant, groupe.get_numero(), groupe.get_matiere())
                    index = groupes_initiale.index(groupe)
                    index2 = groupes_initiale.index(groupe2)
                    groupe.set_liste_eleves(liste_grpe1)
                    groupe2.set_liste_eleves(liste_grpe2)
                    groupes_initiale[index] = groupe
                    groupes_initiale[index2] = groupe2
                    #groupes_deja_vu.append(groupe)

                    liste_conflits_new1 = conflits2()
                    conflit_new1 = calcul_conflits(liste_conflits_new1)

                    if (conflit_new1 < memorise_conflits[len(memorise_conflits) - 1]):
                        print("Amélioration. Le nouveau conflit est : ", conflit_new1)
                        memorise_groupe.append(groupes_initiale)
                        memorise_conflits.append(conflit_new1)
                    else:
                        print(" Pas d'amélioration avec ce groupe")
                        cpt += 1
                        groupes_initiale = memorise_groupe[len(memorise_groupe) - 1]
                        for groupe in groupes_initiale:
                            for eleve5 in groupe.get_liste_eleves():
                                modif_student_inscription(eleve5, groupe.get_numero(), groupe.get_matiere())


        liste_conflits_new = conflits2()
        conflit_new = calcul_conflits(liste_conflits_new)

        if(conflit_new < memorise_conflits[len(memorise_conflits)-1]):
            print("Amélioration. Le nouveau conflit est : ", conflit_new)
            memorise_groupe.append(groupes_initiale)
            memorise_conflits.append(conflit_new)
        else:
            print(" pas d'amélioration")
            cpt += 20
            groupes_initiale = memorise_groupe[len(memorise_groupe)-1]
            for groupe in groupes_initiale:
                for eleve5 in groupe.get_liste_eleves():
                    modif_student_inscription(eleve5, groupe.get_numero(), groupe.get_matiere())
    print("Fin des iterations")

    result = []
    result.append(memorise_groupe[0])
    result.append(memorise_conflits[0])
    result.append((memorise_groupe[1]))
    result.append(memorise_conflits[1])
    result.append(memorise_groupe[len(memorise_groupe)-1])
    result.append(memorise_conflits[len(memorise_conflits)-1])

    return result

def algo1_aleatoire():
    groupes_initiale = affectation_etudiants_groupe_aleatoire_p1()
    liste_conflits = conflits1()
    conflit = calcul_conflits(liste_conflits)
    print("La solution initiale a {} conflits".format(conflit))
    #groupes_initiale_tmp = groupes_initiale
    memorise_conflits = []
    memorise_groupe = []
    memorise_groupe.append(groupes_initiale)
    memorise_conflits.append(conflit)



    cpt = 0

    for iteration in range(10):
        if cpt > 5:
            break
        groupes_deja_vu = []
        for groupe in groupes_initiale:
            if matiere_nb_groupe(groupe.get_matiere()) == 1:
                continue
            for groupe2 in groupes_initiale:
                if groupe != groupe2 and groupe.get_matiere() == groupe2.get_matiere() and groupe2 not in groupes_deja_vu:
                    liste1 = []
                    liste2 = []
                    liste_grpe1 = []
                    liste_grpe2 = []
                    for etudiant1 in groupe.get_liste_eleves():
                        liste_grpe1.append(etudiant1)
                    for etudiant2 in groupe2.get_liste_eleves():
                        liste_grpe2.append(etudiant2)

                    for i in range(12):
                        n1 = random.randint(0, len(liste_grpe1)-1)
                        n2 = random.randint(0, len(liste_grpe2)-1)
                        while liste_grpe1[n1] in liste1:
                            n1 = random.randint(0, 20)
                        while liste_grpe2[n2] in liste2:
                            n2 = random.randint(0, 20)
                        eleve1 = liste_grpe1[n1]
                        eleve2 = liste_grpe2[n2]
                        liste1.append(eleve1)
                        liste_grpe1.remove(eleve1)
                        liste2.append(eleve2)
                        liste_grpe2.remove(eleve2)
                    for eleve in liste1:
                        liste_grpe2.append(eleve)
                        modif_student_inscription(eleve, groupe2.get_numero(), groupe2.get_matiere())
                    for etudiant in liste2:
                        liste_grpe1.append(etudiant)
                        modif_student_inscription(etudiant, groupe.get_numero(), groupe.get_matiere())
                    index = groupes_initiale.index(groupe)
                    index2 = groupes_initiale.index(groupe2)
                    groupe.set_liste_eleves(liste_grpe1)
                    groupe2.set_liste_eleves(liste_grpe2)
                    groupes_initiale[index] = groupe
                    groupes_initiale[index2] = groupe2
                    #groupes_deja_vu.append(groupe)

                    liste_conflits_new1 = conflits1()
                    conflit_new1 = calcul_conflits(liste_conflits_new1)

                    if (conflit_new1 < memorise_conflits[len(memorise_conflits) - 1]):
                        print("Amélioration. Le nouveau conflit est : ", conflit_new1)
                        memorise_groupe.append(groupes_initiale)
                        memorise_conflits.append(conflit_new1)
                    else:
                        print(" Pas d'amélioration avec ce groupe")
                        cpt += 1
                        groupes_initiale = memorise_groupe[len(memorise_groupe) - 1]
                        for groupe in groupes_initiale:
                            for eleve5 in groupe.get_liste_eleves():
                                modif_student_inscription(eleve5, groupe.get_numero(), groupe.get_matiere())


        liste_conflits_new = conflits1()
        conflit_new = calcul_conflits(liste_conflits_new)

        if(conflit_new < memorise_conflits[len(memorise_conflits)-1]):
            print("Amélioration. Le nouveau conflit est : ", conflit_new)
            memorise_groupe.append(groupes_initiale)
            memorise_conflits.append(conflit_new)
        else:
            print(" pas d'amélioration")
            cpt += 20
            groupes_initiale = memorise_groupe[len(memorise_groupe)-1]
            for groupe in groupes_initiale:
                for eleve5 in groupe.get_liste_eleves():
                    modif_student_inscription(eleve5, groupe.get_numero(), groupe.get_matiere())
    print("Fin des iterations")

    result = []
    result.append(memorise_groupe[0])
    result.append(memorise_conflits[0])
    result.append(memorise_groupe[len(memorise_groupe)-1])
    result.append(memorise_conflits[len(memorise_conflits)-1])

    return result
