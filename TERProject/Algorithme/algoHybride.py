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



semestreChoisi="S2"
nombreCombinaisons=64

#Recup de la liste des etudiants
ListeEtudiants=all_students()


#Recup des modules
ListeModules=all_modules()


#Recup des seances
ListeSeances=all_seances()


#Fonction permettant de récupérer les inscriptions
def recupInscription():
    Inscription = np.arange(len(ListeEtudiants)*len(ListeModules)).reshape(len(ListeEtudiants), len(ListeModules))
    if(semestreChoisi == "S1"):
        for etudiant in ListeEtudiants:
            for module in ListeModules:
                if(etudiant.get_matieres_s1() == module.get_code()):
                    Inscription[ListeEtudiants.index(etudiant)][ListeModules.index(module)] = 1
                else:
                    Inscription[ListeEtudiants.index(etudiant)][ListeModules.index(module)] = 0


    if(semestreChoisi == "S2"):
        for etudiant in ListeEtudiants:
            for module in ListeModules:
                for x in iter(etudiant.get_matieres_s2()):
                    if(x == module.get_intitule()):
                     Inscription[ListeEtudiants.index(etudiant)][ListeModules.index(module)] = 1
                    else:
                     Inscription[ListeEtudiants.index(etudiant)][ListeModules.index(module)] = 0

    return Inscription


#Fonction tri des modules dans l'ordre imposé
def ordreModule(modulesNonTries):
    moduleTrie=[]
    for module in ListeModules:
        if module == modulesNonTries[0]:
            moduleTrie.append(modulesNonTries[0])
        if module == modulesNonTries[1]:
            moduleTrie.append(modulesNonTries[1])
        if module == modulesNonTries[2]:
            moduleTrie.append(modulesNonTries[2])
        if module == modulesNonTries[3]:
            moduleTrie.append(modulesNonTries[3])
    return moduleTrie


#Fonction qui récupère seulement les modules
def recupModules(moduleDonne):
    for x in ListeSeances:
        if moduleDonne == x.get_matiere():
            return True
    return False


#Fonction générant les combinaisons => à virer les combi avec les modules de réseaux
def generationCombinaisons():
    modulesNonTries=[]
    j=0
    listeCombinaisons=np.arange(nombreCombinaisons).reshape(16,4)
    for module1 in ListeModules:
        for module2 in ListeModules:
            for module3 in ListeModules:
                for module4 in ListeModules:
                    if (recupModules(module1) & recupModules(module2) & recupModules(module3) & recupModules(module4)):
                        if (module1!= module2) & (module1 != module3) & (module1 != module4) & (module2 != module3) & (module2 != module4) & (module3 != module4):
                            modulesNonTries.append(module1)
                            modulesNonTries.append(module2)
                            modulesNonTries.append(module3)
                            modulesNonTries.append(module4)
                            modulesTries=ordreModule(modulesNonTries)
                            listeCombinaisons[j][0]=modulesTries[0]
                            listeCombinaisons[j][1]=modulesTries[1]
                            listeCombinaisons[j][2]=modulesTries[2]
                            listeCombinaisons[j][3]=modulesTries[3]
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
    indice=0
    modulesTrouves=[]
    listeCombinaisons=generationCombinaisons()
    cptCombinaisons=generationCombinaisons()
    Inscriptions=recupInscription()
    y = 0
    for i in Inscriptions[i][j]:        #parcours etudiant par etudiant
        for j in Inscriptions[i][j]:          #parcours module par module
            if Inscriptions[i][j] == 1:
                modulesTrouves.append(j)
        modulesTrouves=ordreModule(modulesTrouves)
        for x in listeCombinaisons[x][y]:    #parcours combi par combi
            if listeCombinaisons[x][y]==modulesTrouves:
                cptCombinaisons[x]=cptCombinaisons[x]+1
                y = y + 1
    return cptCombinaisons


#Fonction qui va trier dans l'ordre décroissant cptCombinaisons
def triCptCombinaisons():
    cptCombinaisons=calculCptCombinaisons()
    newCptCombinaisons=[]
    max = 0
    for y in cptCombinaisons:
        for x in cptCombinaisons:
            if x > max:
                max = x
        newCptCombinaisons.append(x)
    return newCptCombinaisons


#Fonction qui va trier dans l'ordre décroissant listeCombinaisons
def triListeCombinaisons():
    listeCombinaisons=generationCombinaisons()
    cptCombinaisons=calculCptCombinaisons()
    newCptCombinaisons=[]
    newListeCombinaisons=[]
    max = 0
    for y in cptCombinaisons:
        for x in cptCombinaisons:
            if x > max:
                max = x
        newCptCombinaisons.append(x)
        for i in listeCombinaisons[x][i]:
            newListeCombinaisons.append(listeCombinaisons[x][i])
    return newListeCombinaisons


#Fonction qui va selectionner des combi dans la listeCombinaisons contenant un module donné
def selectionListeCombinaisons(moduleDonne):
    listeCombinaisons=triListeCombinaisons()
    newListeIndex=[]
    newListeCombinaisons=np.arange(nombreCombinaisons).reshape(16,4)
    for x in listeCombinaisons[x][y]:
        for y in listeCombinaisons[x][y]:
            if y == moduleDonne:
                newListeIndex.append(x)
    for x in listeCombinaisons[x][y]:
        for y in listeCombinaisons[x][y]:
            for k in newListeIndex:
                if x == k:
                    newListeCombinaisons.append(listeCombinaisons[x][y])
    return newListeCombinaisons


#Algorithme glouton pour remplir les groupes avec la listeCombinaison


#Algorithme pour optimiser
