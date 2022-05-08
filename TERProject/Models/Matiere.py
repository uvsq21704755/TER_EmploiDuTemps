class Matiere:
    def __init__(self, code, intitule,nbGroupes):
        self.code = code
        self.intitule = intitule
        self.nbGroupes = nbGroupes
    def get_code(self):
        return self.code
    def get_intitule(self):
        return self.intitule
    def get_nbGroupes(self):
        return self.nbGroupes
    def set_nbGroupes(self, nbGroupes):
        self.nbGroupes = nbGroupes
    def affichage(self):
        print("Le module : ", self.intitule, " ", self.code, " contient ", self.nbGroupes, " groupes;")