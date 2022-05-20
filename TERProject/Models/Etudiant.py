class Etudiant:
    def __init__(self, num_etudiant, nom, prenom, formation, matieres_s1, matieres_s2):
        self.num_etudiant = num_etudiant
        self.nom = nom
        self.prenom = prenom
        self.formation = formation
        self.matieres_s1 = matieres_s1
        self.matieres_s2 = matieres_s2
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
    def set_matieres_s1(self, matieres_s1):
        self.self.matieres_s1 = matieres_s1
    def get_matieres_s1(self):
        return self.matieres_s1
    def set_matieres_s2(self, matieres_s2):
        self.self.matieres_s2 = matieres_s2
    def get_matieres_s2(self):
        return self.matieres_s2
    def affichage(self):
        print("L'étudiant : ", self.nom, " ", self.prenom, " ", self.num_etudiant, " est en ", self.formation, "et suit les cours suivant :", self.matieres_s2, self.matieres_s1)
