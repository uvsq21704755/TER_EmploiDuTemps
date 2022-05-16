
class Groupe:
    def __init__(self, matiere, numero, nb_eleves):
        self.numero = numero
        self.matiere = matiere
        self.nb_eleves = nb_eleves
        self.liste_eleves = None
    def get_numero(self):
        return self.numero
    def get_matiere(self):
        return self.matiere
    def get_nbeleves(self):
        return self.nb_eleves
    def set_nb_eleves(self, nb_eleves):
        self.nb_eleves = nb_eleves
    def get_liste_eleves(self):
        return self.liste_eleves
    def set_liste_eleves(self, liste_eleves):
        self.liste_eleves = liste_eleves
    def affichage(self):
        print(self.matiere, "Groupe" , self.numero, self.nb_eleves, "liste des eleves : ")
        for etudiant in self.liste_eleves:
            print(etudiant)
