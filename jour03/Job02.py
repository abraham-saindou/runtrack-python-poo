class CompteBancaire:
    def __init__(self, account_num, nom, prenom, solde):
        self.__account_num = account_num
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde

    def infos(self):
        print(f"Numéro de compte : {self.__prenom}\nNom : {self.__nom}\nPrenom : {self.__prenom}\n Solde : {self.__solde}")

    def afficher_solde(self):
        print(f"Solde : {self.__solde}")

    def versement(self):
        pass

    def retrait(self):
        pass

    def agios(self):
        pass

    def virement(self):
        pass