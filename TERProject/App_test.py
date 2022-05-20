from BD.Creation_tables import (create_tables,delete_all)
from BD.Insertions import insertions_bd
from BD.Recuperations import (all_students,all_instructor,all_formations,all_modules, all_creneaux, all_rooms, all_seances, matiere_nb_groupe, matiere_nb_eleves, verif_affectation,seances_etudiant)
from BD.Modifications import modif_student_inscription
from Algorithme.Donnees import (liste_combinaisons_s1,affectation_combi_etudiant_s1,creation_groupe,affectation_etudiants_groupe_s1,conflits,calcul_conflits)
from Algorithme.algoHybride import (recupInscription)

if __name__ == '__main__':
  print("Bonjour ! Souhaitez-vous tester l'application ou entrer vos donnees ?")
  reponse = input("Repondez par 'Test' ou 'Entrer' : ")
  if reponse == 'Test':
    delete_all()
    create_tables()
    Inscription = recupInscription()
    print(Inscription)
    
  elif reponse == 'Entrer':
    create_tables()
    delete_all()
    insertions_bd()
  else:
    print("Nous n'avons pas compris votre choix")
  # create_tables()
