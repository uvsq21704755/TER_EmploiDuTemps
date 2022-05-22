from BD.Creation_tables import (create_tables,delete_all)
from BD.Insertions import (insertions_bd,insert_etudiant)
from BD.Recuperations import (all_students,all_instructor,all_formations,all_modules, all_creneaux, all_rooms, all_seances, matiere_nb_groupe, matiere_nb_eleves, verif_affectation,seances_etudiant_p1,return_groupe_etudiant,all_seances_p1, all_seances_p2)
from BD.Modifications import (modif_student_inscription,modif_seance,supp_student_inscription)
from Algorithme.Donnees import (liste_combinaisons_p1,liste_combinaisons_p2,affectation_combi_etudiant_p1,creation_groupe_p1,affectation_etudiants_groupe_p1,conflits1, calcul_conflits, algo)
if __name__ == '__main__':

    print("Bonjour. Vous avez le choix entre :")
    liste_choix = [" a : tester l'application "," b : tester l'application et faire des modifications", " c: insérer mes propres données" ]
    for item in liste_choix:
        print(item)
    choix = input("Que choisissez-vous ? : ")

    while choix != "a" or choix != "b" or choix != "c":
        if choix == "a":
            delete_all()
            create_tables()
            print("Patientez, nous calculons les groupes ... ")
            mesgroupes = algo()
            print("Liste des groupes avant amélioration avec {} conflits".format(mesgroupes[1]))
            groupe_initial = mesgroupes[0]
            for groupe in groupe_initial:
                groupe.affichage()
            print("Liste des groupes après amélioration avec {} conflits".format(mesgroupes[5]))
            groupe_final = mesgroupes[4]
            for groupe in groupe_final:
                groupe.affichage()
        if choix == "b":
            delete_all()
            create_tables()
            print("Patientez, nous calculons les groupes ... ")
            algo()
            choix_modif = input("Voulez-vous apporter des modifications ? Répondez par oui ou non : ")

            if choix_modif == "oui":
                print("Vous avez le choix entre :")
                liste_choix2 = [" a : modifier une séance de cours ", " b : modifier la liste des modules auxquels un étudiant est inscrit"]
                for item in liste_choix2:
                    print(item)
                choix2 = input("Que choisissez-vous ? : ")
                arret = 0
                if choix2 == "a":
                    choix22 = input("Voulez-vous modifier les séances de la 1ere partie ou de la 2e partie ? Répondez par 1 ou 2 : ")
                    if choix22 == "1":
                        while arret != 1:
                            #afficher liste séance
                            seances = all_seances_p1()
                            print("Voici la liste des séances : ")
                            for seance in seances:
                                seance.affichage()
                            creneaux = all_creneaux()
                            print("Voici les créneaux disponibles")
                            for creneau in creneaux:
                                creneau.affichage()
                            choix_seance = input("Entrer le numero de la séance que vous souhaitez modifier : ")
                            choix_creneau = input("Entrer les modifications pour le creneau, en choisissant un numero de créneau parmi la liste ci-dessus : ")
                            #mettre à jour la séance
                            modif_seance(choix_seance,choix_creneau)
                            choix23 = input("Avez-vous d'autres modifications à apporter pour les séances ? Répondez par oui ou non : ")
                            if choix23 == "non":
                                arret = 1
                        choix24 = input("Modifications terminées. Voulez-vous relancer l'algorithme ? Répondez par oui ou non :  ")
                        if choix24 == "oui":
                            algo()
                    else:
                        while arret != 1:
                            #afficher liste séance
                            seances = all_seances_p2()
                            print("Voici la liste des séances : ")
                            for seance in seances:
                                seance.affichage()
                            creneaux = all_creneaux()
                            print("Voici les créneaux disponibles")
                            for creneau in creneaux:
                                creneau.affichage()
                            choix_seance = input("Entrer le numero de la séance que vous souhaitez modifier : ")
                            choix_creneau = input("Entrer les modifications pour le creneau, en choisissant un numero de créneau parmi la liste ci-dessus : ")
                            #mettre à jour la séance
                            modif_seance(choix_seance,choix_creneau)
                            choix23 = input("Avez-vous d'autres modifications à apporter pour les séances ? Répondez par oui ou non : ")
                            if choix23 == "non":
                                arret = 1
                        choix24 = input("Modifications terminées. Voulez-vous relancer l'algorithme ? Répondez par oui ou non :  ")
                        if choix24 == "oui":
                            algo()
                else:
                    while arret != 1:
                        # afficher liste des étudiants
                        print("Voici la liste des étudiants")
                        etudiants = all_students()
                        for etudiant in etudiants:
                            etudiant.affichage()
                        choix25 = int(input("Entrer le numero étudiant que vous voulez modifier :"))
                        #afficher liste des matieres auxquels il est inscrit
                        choix26 = input("Choisissez le code de matiere que vous voulez supprimer : ")
                        #afficher liste matiere disponible
                        matieres = all_modules()
                        print("Voici la liste des matieres :")
                        for matiere in matieres:
                            matiere.affichage()
                        choix27 = input("Choisissez le code de matiere que vous voulez insérer : ")
                        choix28 = int(input("Assignez-lui un numero de groupe par défaut : "))
                        #mettre a jour l'etudiant
                        supp_student_inscription(choix25,choix26)
                        insert_etudiant(choix25,choix27,choix28)
                        choix29 = input(
                            "Avez-vous d'autres modifications à apporter pour les étudiants ? Répondez par oui ou non : ")
                        if choix29 == "non":
                            arret = 1
                    choix211 = input("Modifications terminées. Voulez-vous relancer l'algorithme ? Répondez par oui ou non :  ")
                    if choix211 == "oui":
                        algo()
        elif choix == "c":
            insertions_bd()



