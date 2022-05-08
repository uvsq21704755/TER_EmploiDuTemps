class Enseignant:
    def __init__(self, id, nom, prenom, liste_matieres):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.liste_matieres = liste_matieres
    def get_id(self):
        return self.id
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def get_liste_matieres(self):
        return self.liste_matieres
    def set_id(self, id):
        self.id = id
    def set_liste_matieres(self, liste_matieres):
        self.liste_matieres = liste_matieres
    def set_prenom(self, prenom):
        self.prenom = prenom
    def set_nom(self, nom):
        self.nom = nom
    def afficher(self):
        print("L'enseignant : ", self.nom, " ", self.prenom, " ", self.id, " ", self.liste_matieres)