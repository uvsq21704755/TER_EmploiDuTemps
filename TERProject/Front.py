import tkinter as tk 
from tkinter import filedialog, Text
import os 
from tkinter.filedialog import asksaveasfile

# Affichage des deux EDT
def M1_S1_P2():
    choix.set("M1_S1_P2")
    f2 = tk.Frame(root, bg="#FFFFFF", bd=10)
    f2.place(width = 420, height = 250, y=150, x=100)
    days = tk.Label(root, text = "Lundi              Mardi              Mercredi              Jeudi              Vendredi")
    days.place(width=420, height=20, y = 150, x = 100)
    d2 = tk.Label(root, text = "9h40-12h50\nConception\nBD CM\n- - - - \n\n- - - - \n13h50-18h40\nConception\nBD G1\n",bg="#FFFFFF")
    d2.place(width=70, height=185, y = 170, x = 190)
    d3 = tk.Label(root, text = "9h40-12h50\nMéthode de\nRanking CM\n- - - - \n\n- - - - \n13h50-18h40\nConception\nBD G2\n- - - - \n13h50-18h40\nMéthode de\nRanking G1",bg="#FFFFFF")
    d3.place(width=75, height=230, y = 170, x = 270)
    d4 = tk.Label(root, text = "9h40-12h50\nAWS CM\n- - - - \n\n- - - - \n13h50-18h40\nAWS TD\n- - - - \n13h50-18h40\nTuning G2", bg="#FFFFFF")
    d4.place(width=70, height=210, y = 170, x = 350)
    d5 = tk.Label(root, text = "9h40-12h50\nTuning CM\n- - - - \n\n- - - - \n13h50-18h40\nTuning G1\n- - - - \n13h50-18h40\nMéthode de\nRanking G2", bg="#FFFFFF")
    d5.place(width=70, height=225, y = 170, x = 430)

def M1_S1_P1():
    choix.set("M1_S1_P1")
    f2 = tk.Frame(root, bg="#FFFFFF", bd=10)
    f2.place(width = 420, height = 250, y=150, x=100)
    days = tk.Label(root, text = "Lundi              Mardi              Mercredi              Jeudi              Vendredi")
    days.place(width=420, height=20, y = 150, x = 100)
    d1 = tk.Label(root, text = "8h30-11h30\nAnglais G1\n- - - - \n9h40-12h50\nRéseaux Etendus\n- - - - \n\n- - - - \n13h30-16h30\nAnglais G2\n- - - - \n13h50-18h40\nRéseaux Etendus", bg = "#FFFFFF")
    d1.place(width=90, height=225, y = 175, x = 100)
    d2 = tk.Label(root, text = "\n\n\n9h40-12h50\nGLP CM\n- - - - \n\n- - - - \n13h50-18h40\nGLP G1\n- - - - \n13h50-18h40\nCalcul\nSecurisé G2",bg="#FFFFFF")
    d2.place(width=68, height=210, y = 190, x = 190)
    d3 = tk.Label(root, text = "\n\n9h40-12h50\nIP CM\n- - - - \n\n- - - - \n13h50-18h40\nIP TD\n- - - - \n13h50-18h40\nGLP G2", bg="#FFFFFF")
    d3.place(width=68, height=210, y = 190, x = 270)
    d4 = tk.Label(root, text = "8h-12h50\nSimulation G2\n- - - - \n9h-11h\nCalcul\nSécurisé CM\n- - - - \n\n- - - - \n13h-16h\nAnglais G3\n- - - - \n13h50-18h40\nCalcul\nSecurisé G2", bg="#FFFFFF")
    d4.place(width=90, height=230, y = 170, x = 340)
    d5 = tk.Label(root, text = "\n\n9h40-12h50\nSimulation CM\n- - - - \n\n- - - - \n13h50-18h40\nSimulation G1\n- - - - \n13h50-18h40\nGLP G3",bg="#FFFFFF")
    d5.place(width=80, height=190, y = 195, x = 430)

#Initialisation de la fenêtre
root = tk.Tk()
root.title("Formation de Groupes d'Etudiants")
canvas = tk.Canvas(root, height=500, width=700, bg="#ABABAB")
canvas.pack()

#Titre
f1 = tk.Frame(root, bg="#FFFFFF", bd=10)
f1.place(width=400,height=50, y = 50, x = 100)
l1 = tk.Label(root, text = "Bonjour, veuillez choisir votre edt")
l1.place(width=400,height=50, y = 50, x = 100)

#Visualisation des EDT
f2 = tk.Frame(root, bg="#FFFFFF", bd=10)
f2.place(width = 420, height = 250, y=150, x=100)

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
    #App(choix.get())

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
