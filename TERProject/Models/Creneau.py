from psycopg2 import *
import psycopg2
from BD.Connexion import (connexion, close_connexion)

class Creneau:
    def __init__(self, id, jour, hdeb, hfin):
        self.id = id
        self.jour = jour
        self.hdeb = hdeb
        self.hfin = hfin
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
        print("Le ", self.id, "e creneau est : ", self.jour, " de ", self.hdeb, " à ", self.hfin)