class Salle:
    def __init__(self, nom, type_salle, capacite):
        self.nom = nom
        self.capacite = capacite
        self.type_salle = type_salle
    def get_nom(self):
        return self.nom
    def get_capacite(self):
        return self.capacite
    def get_typesalle(self):
        return self.type_salle
    def affichage(self):
        print("La salle", self.nom, " est une salle de", self.type_salle, " et peut accueillir jusqu'à", self.capacite, "eleves")