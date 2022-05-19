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

    Inscription = [] 
    listeModulesSemestre=recupModulesSemestre()

    counterInscription = 0
    
    if(semestreChoisi == "S1"):
        
        for etudiant in ListeEtudiants:
        
            for module in listeModulesSemestre:
            
                for x in etudiant.get_matieres_s1():
                
                    if(x == module):
                        Inscription.append(1)
                    else:
                        Inscription.append(0)
    
    if(semestreChoisi == "S2"):
       
        for etudiant in ListeEtudiants:
            
            for module in listeModulesSemestre:
            
                for x in etudiant.get_matieres_s2():
                
                    if(x == module):
                        Inscription.append(1)
                        counterInscription = counterInscription + 1
                    else:
                        Inscription.append(0)
    
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

#Fonction qui incrémente Cpt
def calculCptCombinaisons():
    cptCombinaisons = []
    cpt=0
    while(cpt < nombreCombinaisons):
        cptCombinaisons.append(0)
        cpt=cpt+1
    modulesTrouves=[]
    listeCombinaisons=generationCombinaisons()
    Inscriptions=recupInscription()
    x=0
    y=0
    dd=0
    for x in Inscriptions:
        for y in Inscriptions:
            if y == 1:
                dd=dd+1

    print(dd)
    y = 0
    i=0
    j=0
    for i in Inscriptions:
        for j in Inscriptions:
            if Inscriptions==1:
                modulesTrouves.append(j)
            modulesTrouves=ordreModule(modulesTrouves)
            for x in listeCombinaisons:    #parcours combi par combi
                if x==modulesTrouves:
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
