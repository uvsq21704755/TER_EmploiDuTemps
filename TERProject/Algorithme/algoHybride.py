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
        #print("-----")
        #print(module.get_intitule())
        #print(modulesNonTries)
        if module.get_intitule() == modulesNonTries[0]:
            moduleTrie.append(modulesNonTries[0])
        if module.get_intitule() == modulesNonTries[1]:
            moduleTrie.append(modulesNonTries[1])
        if module.get_intitule() == modulesNonTries[2]:
            moduleTrie.append(modulesNonTries[2])
        if module.get_intitule() == modulesNonTries[3]:
            moduleTrie.append(modulesNonTries[3])
        #print("apres append: "+str(moduleTrie))
    #print(moduleTrie)    
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
    listeCombinaisons = []
    for module1 in ListeModules:
        for module2 in ListeModules:
            for module3 in ListeModules:
                for module4 in ListeModules:
                    if (recupModules(module1.get_intitule()) and recupModules(module2.get_intitule()) and recupModules(module3.get_intitule()) and recupModules(module4.get_intitule())):
                        if (module1.get_intitule() != module2.get_intitule()) and (module1.get_intitule() != module3.get_intitule()) and (module1.get_intitule() != module4.get_intitule()) and (module2.get_intitule() != module3.get_intitule()) and (module2.get_intitule() != module4.get_intitule()) and (module3.get_intitule() != module4.get_intitule()):
                            modulesNonTries.append(module1.get_intitule())
                            modulesNonTries.append(module2.get_intitule())
                            modulesNonTries.append(module3.get_intitule())
                            modulesNonTries.append(module4.get_intitule())
                            modulesTries=ordreModule(modulesNonTries)
                            listeCombinaisons.append(modulesTries)
                            modulesNonTries.remove(module1.get_intitule())
                            modulesNonTries.remove(module2.get_intitule())
                            modulesNonTries.remove(module3.get_intitule())
                            modulesNonTries.remove(module4.get_intitule())
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
