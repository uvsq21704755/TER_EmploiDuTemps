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

semestreChoisi="S1"
nombreCombinaisons=64

#Recup de la liste des etudiants
ListeEtudiants=all_students()


#Recup des modules
ListeModules=all_modules()


#Fonction permettant de récupérer les inscriptions
def recupInscription():
    Inscription = np.arange(len(ListeEtudiants)*len(ListeModules)).reshape(len(ListeEtudiants), len(ListeModules))
    if(semestreChoisi == "S1"):
        for etudiant in ListeEtudiants:
            for module in ListeModules:
                if(etudiant.get_matieres_s1() == module.get_code()):
                    Inscription[etudiant][module] = 1
                else:
                    Inscription[etudiant][module] = 0

    if(semestreChoisi == "S2"):
        for etudiant in ListeEtudiants:
            for module in ListeModules:
                if(etudiant.get_matieres_s2() == module.get_code()):
                    Inscription[etudiant][module] = 1
                else:
                    Inscription[etudiant][module] = 0               
    return Inscription


#Fonction tri des modules dans l'ordre imposé
def ordreModule(module1, module2, module3, module4):
    moduleTrie=[]
    for module in ListeModules:
        if module == module1:
            moduleTrie.append(module1)
        if module == module2:
            moduleTrie.append(module2)
        if module == module3:
            moduleTrie.append(module3)
        if module == module4:
            moduleTrie.append(module4)
    return moduleTrie


#Fonction générant les combinaisons => à virer les combi avec les modules de réseaux
def generationCombinaisons():
    j=0
    listeCombinaisons=np.arange(nombreCombinaisons).reshape(4,16)
    for module1 in ListeModules:
        for module2 in ListeModules:
            for module3 in ListeModules:
                for module4 in ListeModules:
                    if (module1!= module2) & (module1 != module3) & (module1 != module4) & (module2 != module3) & (module2 != module4) & (module3 != module4):
                        modulesTries=ordreModule(module1, module2, module3, module4)
                        listeCombinaisons[0][j]=modulesTries[0]
                        listeCombinaisons[1][j]=modulesTries[1]
                        listeCombinaisons[2][j]=modulesTries[2]
                        listeCombinaisons[3][j]=modulesTries[3]
                        j=j+1
    return listeCombinaisons


#Fonction générant le cptCombinaisons (effectif d'etudiants pour chacun des combinaisons)
def generationCptCombinaisons():
    cptCombinaisons=[]
    i=0
    while(i < nombreCombinaisons):
        cptCombinaisons[i]=0
        i=i+1
    return cptCombinaisons


#Fonction qui incrémente Cpt
def calculCptCombinaisons():
    listeCombinaisons=generationCombinaisons()
    cptCombinaisons=generationCombinaisons()
    Inscriptions=recupInscription()
    