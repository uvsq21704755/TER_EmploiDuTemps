from BD.Creation_tables import (create_tables,delete_all)
from BD.Insertions import insertions_bd
from BD.Recuperations import (all_students,all_instructor,all_formations,all_modules, all_creneaux, all_rooms, all_seances, matiere_nb_groupe, matiere_nb_eleves, verif_affectation)
from BD.Modifications import modif_student_inscription
from Algorithme.Donnees import (liste_combinaisons,affectation_combi_etudiant,creation_groupe,affectation_etudiants_groupe)
if __name__ == '__main__':
  print("Bonjour ! Souhaitez-vous tester l'application ou entrer vos données ?")
  reponse = input("Répondez par 'Test' ou 'Entrer' : ")
  if reponse == 'Test':
    delete_all()
    create_tables()
    groupes = affectation_etudiants_groupe()
    for groupe in groupes:
      groupe.affichage()
    #groupes = creation_groupe()
    #for groupe in groupes:
     # groupe.affichage()
    #affectations = affectation_combi_etudiant()
    #print(affectations)
    #a = 0
    #for affect in affectations:
    #  for combi in affect:
    #    a = a + (len(affect)-1)
    #print(a)

    #l = liste_combinaisons()
    #print(len(l))
    #print(l)
    # modif_student_inscription(21704755,2,'MIN17217')
    # all_seances()
    # all_rooms()
    # all_creneaux()
    # all_modules()
    #all_formations()
    # all_instructor()
    # all_students()
  elif reponse == 'Entrer':
    create_tables()
    delete_all()
    insertions_bd()
  else:
    print("Nous n'avons pas compris votre choix")
  # create_tables()
