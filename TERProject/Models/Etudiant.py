class Etudiant:
    def __init__(self, num_etudiant, nom, prenom, formation, liste_matieres):
        self.num_etudiant = num_etudiant
        self.nom = nom
        self.prenom = prenom
        self.formation = formation
        self.liste_matieres = liste_matieres
    def get_numetudiant(self):
        return self.num_etudiant
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def get_formation(self):
        return self.formation
    def set_formation(self,formation):
        self.formation = formation
    def set_liste_matieres(self, liste_matieres):
        self.liste_matieres = liste_matieres
    def get_liste_matieres(self):
        return self.liste_matieres
    def affichage(self):
        print("L'étudiant : ", self.nom, " ", self.prenom, " ", self.num_etudiant, " est en ", self.formation, "et suit les cours suivant :", self.liste_matieres)