
class Groupe:
    def __init__(self, numero, nb_eleves, matiere):
        self.numero = numero
        self.matiere = matiere
        self.nb_eleves = nb_eleves
        self.liste_eleves = None
    def get_numero(self, numero):
        return self.numero
    def get_matiere(self):
        return self.matiere
    def get_nbeleves(self):
        return self.nb_eleves
    def get_liste_eleves(self):
        return self.liste_eleves
    def set_liste_eleves(self, liste_eleves):
        self.liste_eleves = liste_eleves