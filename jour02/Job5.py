class Voiture:
    def __init__(self, marque, modele, annee, nb_km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__nb_km = nb_km
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def get_model(self):
        return self.__model

    def get_annee(self):
        return self.__annee

    def get_nb_km(self):
        return self.__nb_km

    def get_status(self):
        return self.__en_marche

    def set_marque(self, marque):
        self.get_marque()
        self.__marque = marque

    def set_model(self, model):
        self.get_model()
        self.__model = model

    def set_annee(self, annee):
        self.get_annee()
        self.__annee = annee

    def set_nb_km(self, nb_km):
        self.get_nb_km()
        self.__marque = nb_km

    def set_status(self):
        status = self.get_status()
        if not status:
            self.__en_marche = True
        else:
            self.__en_marche = False
        return self.__en_marche

    def demarrer(self):
        pass

    def arreter(self):
        pass

    def __verifier_plein(self):
        pass