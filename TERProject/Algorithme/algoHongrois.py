from http.client import NETWORK_AUTHENTICATION_REQUIRED
from typing import List
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
import numpy as np



#FONCTIONS DE PREPARATION
# Fonction qui recupere seulement les etudiants inscrits dans un module
def recupEtudiants(moduleVoulu):

    listeEtudiants=all_students()
    newListEtudiants = []

    for etudiant in listeEtudiants:
       if(etudiant.get_matieres_s1() ==  moduleVoulu) :
            newListEtudiants.append(etudiant.get_numetudiant());

    print(newListEtudiants)
    return newListEtudiants


# Fonction qui genere aleatoirement les etudiants dans des groupes pour un module
def randomGroupe(nbEtudiant, nbGroupe):
    Matrice = np.arange(nbEtudiant*nbGroupe).reshape(nbEtudiant,nbGroupe)

    for i in range (nbEtudiant) :
        for j in range(nbGroupe-1) : 
            r = np.random.randint(2)
            Matrice[i,j] = r 
            j += 1
            if(r == 0) :
                Matrice[i,j] = 1
            else :
                Matrice[i,j] = 0
    return Matrice


# Fonction qui stocke tous les groupes pour un module



# MATRICE AFFECTATION
# Creation de la matrice d'affectation :
# 0 si pas affecté, 1 si affecté


# Creation de la matrice des couts d'affectation :
#si il a cours module fonda sur le meme creneau 
#si il a cours module optionnel sur le meme creneau
#si il a cours module general sur le meme creneau 





# ALGORITHME HONGROIS
# Transformation de la matrice d'affectation n*m en n*n
#def equilibrageMatrice():
    #if(len(n) < len(m)):
        #extend la matrice de n à n+(m-n) et remplir de 0
    #if(len(m)<len(n)):
        #extend la matrice de m à m+(n-m) et remplir de 0