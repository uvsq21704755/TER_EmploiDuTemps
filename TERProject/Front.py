import tkinter as tk 
from tkinter import filedialog, Text
import os 
from tkinter.filedialog import asksaveasfile
from App.py import App

# Définitions des fonctions

def M1_S1_P1():
    choix.set("M1_S1_P1")
    f2 = tk.Frame(root, bg="#FFFFFF", bd=10)
    f2.place(width = 400, height = 200, y=150, x=100)
    days = tk.Label(root, text = "Lundi            Mardi            Mercredi            Jeudi            Vendredi")
    days.place(width=400, height=20, y = 150, x = 100)
    d2 = tk.Label(root, text = "Conception\nBD CM\n- - - - \n\n- - - - \nConception\nBD G1\n\n\n",bg="#FFFFFF")
    d2.place(width=60, height=180, y = 170, x = 190)
    d3 = tk.Label(root, text = "Méthode de\nRanking CM\n- - - - \n\n- - - - \nConception\nBD G2\n- - - - \nMéthode de\nRanking G1",bg="#FFFFFF")
    d3.place(width=75, height=180, y = 170, x = 260)
    d4 = tk.Label(root, text = "AWS CM\n- - - - \n\n- - - - \nAWS TD\n- - - - \nTuning G2\n", bg="#FFFFFF")
    d4.place(width=60, height=180, y = 170, x = 340)
    d5 = tk.Label(root, text = "Tuning CM\n- - - - \n\n- - - - \nTuning G1\n- - - - \nMéthode de\nRanking G2", bg="#FFFFFF")
    d5.place(width=100, height=180, y = 170, x = 400)

def M1_S1_P2():
    choix.set("M1_S1_P2")
    f2 = tk.Frame(root, bg="#FFFFFF", bd=10)
    f2.place(width = 400, height = 200, y=150, x=100)
    days = tk.Label(root, text = "Lundi            Mardi            Mercredi            Jeudi            Vendredi")
    days.place(width=400, height=20, y = 150, x = 100)
    d1 = tk.Label(root, text = "Anglais G1\n- - - - \nRéseaux Etendus\n- - - - \n\n- - - - \nAnglais G2\n- - - - \nRéseaux Etendus", bg = "#FFFFFF")
    d1.place(width=90, height=180, y = 170, x = 100)
    d2 = tk.Label(root, text = "\n\nGLP CM\n- - - - \n\n- - - - \nGLP G1\n- - - - \nCalcul\nSecurisé G2",bg="#FFFFFF")
    d2.place(width=60, height=170, y = 180, x = 190)
    d3 = tk.Label(root, text = "IP CM\n- - - - \n\n- - - - \nIP TD\n- - - - \nGLP G2", bg="#FFFFFF")
    d3.place(width=60, height=120, y = 215, x = 260)
    d4 = tk.Label(root, text = "Simulation G2\n- - - - \nCalcul\nSécurisé CM\n- - - - \n\n- - - - \nAnglais G3\n- - - - \nCalcul\nSecurisé G2", bg="#FFFFFF")
    d4.place(width=90, height=180, y = 170, x = 315)
    d5 = tk.Label(root, text = "\n\nSimulation CM\n- - - - \n\n- - - - \nSimulation G1\n- - - - \nGLP G3",bg="#FFFFFF")
    d5.place(width=100, height=180, y = 170, x = 400)

#Initialisation de la fenêtre
root = tk.Tk()
root.title("Formation de Groupes d'Etudiants")
canvas = tk.Canvas(root, height=400, width=700, bg="#ABABAB")
canvas.pack()

#Titre
f1 = tk.Frame(root, bg="#FFFFFF", bd=10)
f1.place(width=400,height=50, y = 50, x = 100)
l1 = tk.Label(root, text = "Bonjour, veuillez choisir votre edt")
l1.place(width=400,height=50, y = 50, x = 100)

#Visualisation des EDT
f2 = tk.Frame(root, bg="#FFFFFF", bd=10)
f2.place(width = 400, height = 200, y=150, x=100)

#Choix de l'EDT
menuFichier = tk.Menubutton(root, text='Fichier', borderwidth=2, bg='gray', activebackground='darkorange')
menuFichier.place(width=70, height=30, y=75, x=600)
choix = tk.StringVar()

# Création d'un menu défilant
menuDeroulant1 = tk.Menu(menuFichier,tearoff = 0)
menuDeroulant1.add_command(label="M1-S1-P1", command = M1_S1_P1)
menuDeroulant1.add_command(label="M1-S1-P2", command = M1_S1_P2)

# Attribution du menu déroulant au menu Affichage
menuFichier.configure(menu=menuDeroulant1)

# Fonction pour Save
def save_button():
	files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt')]
	file = asksaveasfile(filetypes = files, defaultextension = files)

# Page de résultat
def nextPage():
    root.destroy()

    #Lance le programme
    App(choix)

    #Initialisation de la fenêtre
    r2 = tk.Tk()
    canvas = tk.Canvas(r2, height=400, width=700, bg="#ABABAB")
    canvas.pack()
    print(choix.get())

    #Bouton save
    save = tk.Button(r2, text="Sauvegarder", command = save_button)
    save.place(height=40, width=80,y=310, x=600)

    #Affichage des groupes si possible

    r2.mainloop()

# Bouton continuer
b1 = tk.Button(root, text="Continuer", command = nextPage)
b1.place(height=40, width=80,y=310, x=600)

root.mainloop()