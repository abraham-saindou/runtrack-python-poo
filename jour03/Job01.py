class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def get_cityname(self):
        return self.__nom

    def get_habitants(self):
        return self.__habitants

    def set_habitants(self, add):
        self.get_habitants()
        self.__habitants += add
        print(f"Mise à jour de la population de {self.__nom} : {self.__habitants} habitants.")

    def infos(self):
        print(f"Le nombre d'habitants de {self.__nom} est de {self.__habitants}.")


class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age
        self.__ville = Ville

    def ajouterPop(self, ville: Ville):
        ville.set_habitants(1)
        print(f"{self.__nom}, {self.__age} ans, a été ajouter à {ville.get_cityname()}")


Ville1 = Ville("Paris", 1000000)
Ville2 = Ville("Marseille", 861635)
Ville1.infos()
Ville2.infos()
Pers1 = Personne("John", 45)
Pers2 = Personne("Myrtille", 4)
Pers3 = Personne("Chloé", 18)
Pers1.ajouterPop(Ville1)
Pers2.ajouterPop(Ville1)
Pers3.ajouterPop(Ville2)

