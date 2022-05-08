class Seance:
    def __init__(self, id, jour, hdeb, hfin, salle, enseignant, groupe, matiere):
        self.id = id
        self.jour = jour
        self.hdeb = hdeb
        self.hfin = hfin
        self.salle = salle
        self.groupe = groupe
        self.enseignant = enseignant
        self.matiere = matiere
    def get_salle(self):
        return self.salle
    def get_enseignant(self):
        return self.enseignant
    def get_groupe(self):
        return self.groupe
    def get_matiere(self):
        return self.matiere
    def set_salle(self, salle):
        self.salle = salle
    def set_enseignant(self, enseignant):
        self.enseignant = enseignant
    def set_groupe(self, groupe):
        self.groupe = groupe
    def set_matiere(self, matiere):
        self.matiere = matiere
    def get_id(self):
        return self.id
    def get_hdeb(self):
        return self.hdeb
    def get_hfin(self):
        return self.hfin
    def get_jour(self):
        return self.jour
    def set_hdeb(self, hdeb):
        self.hdeb = hdeb
    def set_hfin(self, hfin):
        self.hfin = hfin
    def set_jour(self, jour):
        self.jour = jour
    def affichage(self):
        print(self.id, ":", self.jour, " ", self.hdeb, "-", self.hfin, ",", self.salle, ",", self.enseignant, ",", self.groupe, ",", self.matiere)



