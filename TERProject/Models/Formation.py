class Formation:
    def __init__(self,nom,code,modules_proposes,options):
        self.nom = nom
        self.code = code
        self.modules_proposes = modules_proposes
        self.options = options

    def get_nom(self):
        return self.nom
    def set_nom(self, nom):
        self.nom = nom
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_modules_proposes(self):
        return self.modules_proposes
    def set_modules(self, modules_proposes):
        self.modules_proposes = modules_proposes
    def get_options(self):
        return self.options
    def set_options(self, options):
        self.options = options
    def affichage(self):
        print("La formation :", self.nom, " ", self.code, "propose les modules suivants : ", self.modules_proposes, "et les options suivantes : ", self.options)