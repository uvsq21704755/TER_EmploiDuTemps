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
nombreCombinaisons=5040

#Recup de la liste des etudiants
ListeEtudiants=all_students()


#Recup des modules
ListeModules=all_modules()


#Recup des seances
ListeSeances=all_seances()

##### Fonction pour récupérer les matières de semestre demandé en paramètre
def recupModulesSemestre():

    listeModulesSemestre=[]

    if(semestreChoisi == "S1"):
        for module in ListeModules:
            for etudiant in ListeEtudiants:
                for x in etudiant.get_matieres_s1():
                    if module.get_intitule() == x:
                        if module.get_intitule() not in listeModulesSemestre:
                            listeModulesSemestre.append(module.get_intitule())

    if(semestreChoisi == "S2"):
        for module in ListeModules:
            for etudiant in ListeEtudiants:
                for x in etudiant.get_matieres_s2():
                    if module.get_intitule() == x:
                        if module.get_intitule() not in listeModulesSemestre:
                            listeModulesSemestre.append(module.get_intitule())
    
    return listeModulesSemestre    

#Fonction permettant de récupérer les inscriptions
def recupInscription():

    Inscription = [[]] 
    listeModulesSemestre = recupModulesSemestre()
    i = 0
    j = 0

    if(semestreChoisi == "S1"):
       
        for etudiant in ListeEtudiants:
            
            tmp = etudiant.get_matieres_s2()

            for module in listeModulesSemestre:
             
                if(tmp[j] == module):
                    Inscription[i][j] = 1
                else:
                    Inscription[i][j] = 0
            j = j + 1
        i = i + 1   

    if(semestreChoisi == "S2"):
       
        for etudiant in ListeEtudiants:
            
            tmp = etudiant.get_matieres_s2()

            for module in listeModulesSemestre:
             
                if(tmp[j] == module):
                    Inscription[i][j] = 1
                else:
                    Inscription[i][j] = 0
            j = j + 1
        i = i + 1

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

#Fonction générant les combinaisons => à virer les combi avec les modules de réseaux
def generationCombinaisons():
    
    modulesNonTries=[]
    listeCombinaisons = []
    ListeModulesSemestre=recupModulesSemestre()
    
    #S1
    if(semestreChoisi == "S1"):

        for module1 in ListeModulesSemestre:
            
            for module2 in ListeModulesSemestre:
                
                for module3 in ListeModulesSemestre:
                    
                    for module4 in ListeModulesSemestre:
                        
                        for module5 in ListeModulesSemestre:
                            
                            if (module1!=module2) and (module1!=module3) and (module1!=module4) and (module1!=module5) and (module2!=module3) and (module2!=module4) and (module2!=module5) and (module3!=module4) and (module3!=module5) and (module4!=module5):

                                modulesNonTries.append(module1)
                                modulesNonTries.append(module2)
                                modulesNonTries.append(module3)
                                modulesNonTries.append(module4)
                                modulesNonTries.append(module5)
                                modulesTries = ordreModule(modulesNonTries)

                                if modulesTries not in listeCombinaisons:
                                    listeCombinaisons.append(modulesTries)

                                modulesNonTries.remove(module1)
                                modulesNonTries.remove(module2)
                                modulesNonTries.remove(module3)
                                modulesNonTries.remove(module4)
                                modulesNonTries.remove(module5)
    #S2
    if(semestreChoisi == "S2"):

        for module1 in ListeModulesSemestre:
            
            for module2 in ListeModulesSemestre:
                
                for module3 in ListeModulesSemestre:
                    
                    for module4 in ListeModulesSemestre:
                        
                        if (module1!=module2) and (module1!=module3) and (module1!=module4) and (module2!=module3) and (module2!=module4) and (module3!=module4):

                            modulesNonTries.append(module1)
                            modulesNonTries.append(module2)
                            modulesNonTries.append(module3)
                            modulesNonTries.append(module4)
                            modulesTries = ordreModule(modulesNonTries)

                            if modulesTries not in listeCombinaisons:
                                listeCombinaisons.append(modulesTries)

                            modulesNonTries.remove(module1)
                            modulesNonTries.remove(module2)
                            modulesNonTries.remove(module3)
                            modulesNonTries.remove(module4)

    return listeCombinaisons

#Fonction qui incrémente Cpt
def calculCptCombinaisons():
    cptCombinaisons = []
    cpt = 0
    while(cpt < nombreCombinaisons):
        cptCombinaisons.append(0)
        cpt = cpt+1
    modulesTrouves = []
    listeCombinaisons = generationCombinaisons()
    Inscriptions = recupInscription()
    x = 0

    y = 0
    i = 0
    j = 0
    #Depuis Inscriptions, retrouver le module correspondant
    #Inscriptions[x:etudiant][y:module]
    listeModulesSemestre = recupModulesSemestre()
    print(Inscriptions)

#    for x in modulesTrouves:
#        modulesTrouves[x] = ordreModule(x)

#    for x in listeCombinaisons:    #parcours combi par combi
#        if x == modulesTrouves:
#            cptCombinaisons[x] = cptCombinaisons[x]+1
#            y = y + 1

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
