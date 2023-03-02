class Vehicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

    def informations_vehicule(self):
        print(f"Marque : {self.marque}\nAnnee : {self.annee}\nPrix en € : {self.prix}")

    def demarrer(self):
        print("Attention, je roule.\n")


class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix):
        Vehicule.__init__(self, marque, model, annee, prix)
        self.portes = 4

    def informations_vehicule(self):
        print(f"Marque : {self.marque}\nAnnee : {self.annee}\nPrix : {str(self.prix)} €\nNombre de portes : {self.portes}")

    def demarrer(self):
        print("Je brûle les feux rouges !\n")


class Moto(Vehicule):
    def __init__(self, marque, model, annee, prix):
        Vehicule.__init__(self, marque, model, annee, prix)
        self.roues = 2

    def informations_vehicule(self):
        print(f"Marque : {self.marque}\nAnnee : {self.annee}\nPrix : {str(self.prix)} €\nNombre de roues : {self.roues}")

    def demarrer(self):
        print("Je prends un virage très serré !\n")


vehi = Vehicule("Renault", "Captur", "2015", 7000)
vehi.informations_vehicule()
vehi.demarrer()
Ford = Voiture("Ford", "GT", "2017", 150000)
Ford.informations_vehicule()
Ford.demarrer()
Yamaha = Moto("Yamaha", "T-Max", "2021", 17000)
Yamaha.informations_vehicule()
Yamaha.demarrer()