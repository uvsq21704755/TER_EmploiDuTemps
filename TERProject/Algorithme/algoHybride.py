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

capaciteGroupe=40
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

    listeModulesSemestre = recupModulesSemestre()
    nbEtu = len(ListeEtudiants)
    nbMod = len(listeModulesSemestre)
    Inscription = [[0 for x in range(nbMod)] for y in range(nbEtu)]
    i = 0
    j = 0

    if(semestreChoisi == "S1"):
       
        for etudiant in ListeEtudiants:
            
            for module in listeModulesSemestre:
             
                if module in etudiant.get_matieres_s1():
                    Inscription[i][j] = 1
                else:
                    Inscription[i][j] = 0
                j = j + 1
                if j == nbMod:
                    j = 0
            i = i + 1 

    if(semestreChoisi == "S2"):
       
        for etudiant in ListeEtudiants:
            
            for module in listeModulesSemestre:
             
                if module in etudiant.get_matieres_s2():
                    
                    Inscription[i][j] = 1
                else:

                    Inscription[i][j] = 0
                
                j = j + 1
                
                if j == nbMod:
                    j = 0
            i = i + 1

    return Inscription

#Fonction tri des modules dans l'ordre imposé
def ordreModule(modulesNonTries):

    moduleTrie=[]
    listeModulesSemestre = recupModulesSemestre()
    nbModNT = len(modulesNonTries)

    for module in listeModulesSemestre:
        #print("-----")
        #print(module.get_intitule())
        #print(modulesNonTries)
        for x in range(0,nbModNT):
            if module == modulesNonTries[x]:
                moduleTrie.append(modulesNonTries[x])
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

def suppressionDoublons():
    listeCombinaisons=generationCombinaisons()
    cpt=0
    for x in listeCombinaisons[x][y]:
        for y in listeCombinaisons[x][y]:
            for k in listeCombinaisons[k][j]:
                for j in listeCombinaisons[k][j]:
                    if y == j:
                        cpt = cpt+1
                    else:
                        cpt = 0
            



#Fonction qui incrémente Cpt
def calculCptCombinaisons():
    cptCombinaisons = []
    cpt = 0
    
    listeCombinaisons = generationCombinaisons()
    Inscriptions = recupInscription()
    j = 0
    idx = 0
    listeModulesSemestre = recupModulesSemestre()
    modulesTrouves = []

    for i in range(0,len(ListeEtudiants)):

            for x in listeModulesSemestre:
                    
                if Inscriptions[i][j] == 1:
                    
                    modulesTrouves.append(x) 

                j = j + 1
                if j == 4:

                    j = 0
                    modulesTrouves = ordreModule(modulesTrouves)
                   
                for y in listeCombinaisons:    #parcours combi par combi
                     
                    if y == modulesTrouves:
                        
                        cptCombinaisons.append(cpt + 1)
                        cpt = cpt + 1
            
            modulesTrouves.clear()

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


#Génération d'un groupe pour un module (glouton)
def generationGroupe(moduleDonnee):

    listeGroupes = []
    groupe = []
    cptGroupe = 0
    nbEtudiants = 0

    """
    if(semestreChoisi=="S1"):
        for etudiant in ListeEtudiants:
            moduleEtudiant=etudiant.get_matieres_s1()
            if moduleDonnee in moduleEtudiant:
                if cptGroupe <= capaciteGroupe:
                    cptGroupe=cptGroupe+1
                    groupe.append(etudiant.get_numetudiant())
                else :
                    cptGroupe = 0
                    listeGroupes.append(groupe)
                    groupe.clear()
        listeGroupes.append(groupe)
    """

    if(semestreChoisi == "S2"):
                
        for etudiant in ListeEtudiants:

            moduleEtudiant = etudiant.get_matieres_s2()
            
            for moduleConsidere in moduleEtudiant:

                if moduleDonnee == moduleConsidere and cptGroupe < capaciteGroupe:
                    
                   cptGroupe = cptGroupe + 1
                   groupe.append(etudiant.get_numetudiant())

                elif cptGroupe >= capaciteGroupe:

                    cptGroupe = 0
                    listeGroupes.append(groupe.copy())
                    groupe.clear()
                    groupe.append(etudiant.get_numetudiant())

            print(cptGroupe)
             
    listeGroupes.append(groupe)

    return listeGroupes
 

def generationTousLesGroupes():

    listeGroupes=[[],[]]

    for module in ListeModules:
       listeGroupes=generationGroupe(module)

    print(listeGroupes)
    return listeGroupes
    


#Génération de tous les groupes pour tous les modules + Création de la matrice Affectation Groupe x Etudiant
def creationMatriceAffectation():

    listeGroupes=generationTousLesGroupes()
    matriceAffectation=[[],[]]



        
    return listeGroupes

#Generation des conditions en fonction des seances

#Passage de la matrice sous conditions 

#Passage de la matrice sous conditions

#Algorithme hongrois

