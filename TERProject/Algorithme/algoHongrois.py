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



""" 
Algorithme hongrois
def recuperationMinColonne (matriceA):
    """Recuperation des min par colonne"""
    col_min_elt = []
    i = 0
    while i < len(matrix):
        col = []
        for y, y_elt in enumerate(matrix):
            for x, x_elt in enumerate(y_elt):
                if x == i:
                    col.append(x_elt)
        min = col[0]
        for elt in col:
            if min > elt:
                min = elt
        col_min_elt.append(min)
        i += 1
    return col_min_elt

def recup_min_line (matrix):
    """Recuperation des min par ligne"""
    line_min_elt = []
    for y_elt in matrix:
        min_line = y_elt[0]
        for x_elt in y_elt:
            if min_line > x_elt:
                min_line = x_elt
        line_min_elt.append(min_line)
    return line_min_elt

def remove_min_col (matrix, list_min_col):
    """Soustraction des min par colonne"""
    i = 0
    while i < len(matrix):
        for y, y_elt in enumerate(matrix):
            for x, x_elt in enumerate(y_elt):
                if x == i:
                    matrix[y][x] = x_elt - list_min_col[i]
        i += 1
    return matrix

def remove_min_line (matrix, list_min_line):
    """Soustraction des min par ligne"""
    for y, y_elt in enumerate(matrix):
        for x, x_elt in enumerate(y_elt):
            matrix[y][x] = x_elt - list_min_line[y]
    return matrix

def min_cout (list_min_col, list_min_line):
    """Calcule du coup minimal"""
    i = 0
    B = 0
    while i < len(list_min_col):
        B += (list_min_col[i] + list_min_line[i])
        i += 1
    return B

# (END) FONCTION DEDIEE A LA PREMIER ETAPE #

# FONCTION DEDIEE A LA SECONDE ETAPE #

def choice_line (matrix):
    """a- Choix de la ligne qui contient le moins de zero libre"""
    line = 0
    liste_nb_zero = list()
    liste_sans_zero = list()
    for line in matrix:
        liste_nb_zero.append(line.count(0))
    for elt in liste_nb_zero:
        if elt != 0:
            liste_sans_zero.append(elt)
    line = liste_nb_zero.index(min(liste_sans_zero))
    return line

def zero_framing (matrix, line):
    """b- Encadrement du premier zero de la ligne et barrer le reste des zeros sur la ligne/colonne
    On designera par E un zero encadre et par B un zero barre"""
    trouver = False
    col = 0
    for x, x_elt in enumerate(matrix[line]):
        if x_elt == 0 and not trouver:
            trouver = True
            col = x
            matrix[line][x] = 'E'
            continue
        if trouver and x_elt == 0:
            matrix[line][x] = 'B'
    for y, y_elt in enumerate(matrix):
        for x, x_elt in enumerate(y_elt):
            if x == col and x_elt == 0:
                matrix[y][x] = 'B' 
    return matrix

def remaining_zero (matrix):
    """Verifie si il reste des zeros non Encadre ou Barre dans la matrice"""
    rest = False
    for y_elt in matrix:
        for x_elt in y_elt:
            if x_elt == 0:
                rest = True
                break
    return rest

 (END) FONCTION DEDIEE A LA SECONDE ETAPE 

FONCTION DEDIEE A LA TROISIEME ETAPE 

def marquage_ligne_a (matrix):
    
    ligne_marque_a = list()
    for y, y_elt in enumerate(matrix):
        if 'E' not in y_elt:
            ligne_marque_a.append(y)
    return ligne_marque_a

def marquage_colonne (matrix, marquage):
    """b- Marque une colonne ayant un zero barre sur une ligne marquee"""
    marquage_effectue = False
    for y, y_elt in enumerate(matrix):
        for x, x_elt in enumerate(y_elt):
            if x_elt == 'B' and y == marquage['ligne'][-1]:
                marquage['colonne'].append(x)
                marquage_effectue = True
    return marquage_effectue
             

def marquage_ligne_c (matrix, marquage):
    """c- Marque une ligne ayant un zero encadre sur une colonne marquee"""
    marquage_effectue = False
    for y, y_elt in enumerate(matrix):
        for x, x_elt in enumerate(y_elt):
            if x_elt == 'E' and x == marquage['colonne'][-1]:
                marquage['ligne'].append(y)
                marquage_effectue = True
    return marquage_effectue

def obtention_marquage (matrix):
    """Renvoie une liste de marquage de la matrice"""
    marquage = {
        'ligne': list(),
        'colonne': list()
    }
    ligne_marque_a = marquage_ligne_a(matrix)
    for ligne_a in ligne_marque_a:
        marquage['ligne'].append(ligne_a)
        while True:
            marquage_effectue = marquage_colonne(matrix, marquage)
            if not marquage_effectue:
                break
            marquage_effectue = marquage_ligne_c(matrix, marquage)
            if not marquage_effectue:
                break
    return marquage

def obtention_sm (matrix, marquage):
    """Renvoie le support minimal sous forme de liste"""
    support_minimal = {
        'ligne': list(),
        'colonne': list()
    }
    support_minimal['colonne'] = marquage['colonne']
    for i in enumerate(matrix):
        if i[0] not in marquage['ligne']:
            support_minimal['ligne'].append(i[0])
    return support_minimal

def count_marquage (marquage):
    """Compte le nombre de marquage effectue"""
    marquage_ligne = marquage['ligne']
    marquage_colonne = marquage['colonne']
    nb = 0
    for elt in marquage_ligne:
       nb_occur = marquage_ligne.count(elt)
       if nb < nb_occur:
           nb = nb_occur
    for elt in marquage_colonne:
        nb_occur = marquage_colonne.count(elt)
        if nb < nb_occur:
            nb = nb_occur
    return nb

# (END) FONCTION DEDIEE A LA TROISIEME ETAPE #

# FONCTION DEDIEE A LA QUATRIEME ETAPE #

def get_min (matrix, support_minimal):
    """Retourne le plus petit nombre du tableau restant"""
    ligne_rayee = support_minimal['ligne']
    colonne_rayee = support_minimal['colonne']
    nb = list()
    for y, y_elt in enumerate(matrix):
        for x, x_elt in enumerate(y_elt):
            if x not in colonne_rayee and y not in ligne_rayee:
                nb.append(x_elt)
    return min(nb)

def deplace_zero (matrix, support_minimal, min_nb):
    
    ligne_rayee = support_minimal['ligne']
    colonne_rayee = support_minimal['colonne']
    for y, y_elt in enumerate(matrix):
        for x, x_elt in enumerate(y_elt):
            if x not in colonne_rayee and y not in ligne_rayee:
                matrix[y][x] = x_elt - min_nb
            elif x in colonne_rayee and y in ligne_rayee:
                matrix[y][x] = x_elt + min_nb
    return matrix

def update_cout_minimal (cout_actuel, nb_marquage, nb_min):
    """Retourne le nonmbre minimal nouveau au cout minimal"""
    return cout_actuel + (nb_min * nb_marquage)

# (END) FONCTION DEDIEE A LA QUATRIEME ETAPE #

# ETAPE DE L'ALGORITHME #

def step_one (matrix, last_min_cost=0):
    
    min_col = recup_min_col(matrix)
    matrix = remove_min_col(matrix, min_col)
    min_line = recup_min_line(matrix)
    matrix = remove_min_line(matrix, min_line)
    cout_min = last_min_cost + min_cout(min_col, min_line)
    return {
        'matrix': matrix,
        'cout_minimal': cout_min,
        'min_col': min_col,
        'min_line': min_line,
    }

def step_two (step_one_response):
    
    matrix = list(step_one_response['matrix'])
    cout_minimal = step_one_response['cout_minimal']
    while remaining_zero(matrix):
        line = choice_line(matrix)
        matrix = zero_framing(matrix, line)
    return {'matrix': matrix, 'cout_minimal': cout_minimal}

def step_three (step_two_response):
    
    matrix = step_two_response['matrix']
    cout_minimal = step_two_response['cout_minimal']
    marquage = obtention_marquage(matrix)
    nb_marquage = count_marquage(marquage)
    support_minimal = obtention_sm(matrix, marquage)
    return {
        'matrix': matrix,
        'cout_minimal': cout_minimal,
        'support_minimal': support_minimal,
        'nb_marquage': nb_marquage,
    }

def step_four (step_three_response):
    
    matrix = step_three_response['matrix']
    old_cout_minimal = step_three_response['cout_minimal']
    support_minimal = step_three_response['support_minimal']
    nb_marquage = step_three_response['nb_marquage']
    matrix = format_matrix(matrix)
    min_nb = get_min(matrix, support_minimal)
    matrix = deplace_zero(matrix, support_minimal, min_nb)
    cout_minimal = update_cout_minimal(old_cout_minimal, nb_marquage, min_nb)
    return {
        'matrix': matrix,
        'old_cout_minimal': old_cout_minimal,
        'cout_minimal': cout_minimal,
        'min_nb': min_nb,
        'support_minimal': support_minimal,
        'nb_marquage': nb_marquage,
    }
"""