from BD.Creation_tables import (create_tables,delete_all)
from BD.Insertions import insertions_bd
from BD.Recuperations import (all_students,all_instructor,all_formations,all_modules, all_creneaux, all_rooms, all_seances)
from BD.Modifications import modif_student_inscription
if __name__ == '__main__':
  print("Bonjour ! Souhaitez-vous tester l'application ou entrer vos données ?")
  reponse = input("Répondez par 'Test' ou 'Entrer' : ")
  if reponse == 'Test':
    delete_all()
    create_tables()
    # modif_student_inscription(21704755,2,'MIN17217')
    # all_seances()
    # all_rooms()
    # all_creneaux()
    # all_modules()
    all_formations()
    # all_instructor()
    # all_students()
  elif reponse == 'Entrer':
    create_tables()
    delete_all()
    insertions_bd()
  else:
    print("Nous n'avons pas compris votre choix")
  # create_tables()
