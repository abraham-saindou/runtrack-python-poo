class CompteBancaire:
    def __init__(self, account_num, nom, prenom, solde, decouvert):
        self.__account_num = account_num
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = decouvert

    def get_solde(self):
        return self.__solde

    def infos(self):
            agios = self.agios()
            print(f"Numéro de compte : {self.__prenom}\nNom : {self.__nom}\nPrenom : {self.__prenom}")
            print(f"Solde : {self.__solde} €\nFrais de compte : {agios} €\n")

    def afficher_solde(self):
        print(f"Le Solde de {self.__nom} {self.__prenom} est de {self.__solde} €\n")

    def versement(self):
        self.get_solde()
        print("Combien d'euros voulez-vous ajouter ?")
        add = int(input("Montant en € : "))
        self.__solde += add
        print(f"{add} € a été ajouté au compte {self.__account_num}")
        self.afficher_solde()

    def retrait(self):
        self.get_solde()
        self.afficher_solde()
        print("Combien d'euros voulez-vous retirer ?")
        withdraw = int(input("Montant en € : "))
        if self.__solde > withdraw or self.decouvert:
            self.__solde -= withdraw
            print(f"{withdraw} € a été retiré du compte.")
        self.afficher_solde()

    def agios(self):
        self.get_solde()
        if self.__solde < 0:
            agios = self.__solde * 0.03
            return agios
        return "0"

    def virement(self, CompteBancaire):
        print("Combien d'euros voulez-vous virer ?")
        montant = int(input("Montant à virer en € : "))
        CompteBancaire.__solde += montant
        print(f"{self.__nom} {self.__prenom} a viré {montant} € dans le compte de {CompteBancaire.__nom} {CompteBancaire.__prenom}")
        CompteBancaire.infos()


Compte1 = CompteBancaire(12, "Alvaro", "Morata", 40000, True)
Compte2 = CompteBancaire(13, "Franck", "Ribéry", 70000, False)
Compte1.infos()
Compte1.retrait()
Compte1.agios()
Compte1.infos()
Compte2.virement(Compte1)
# Compte1.afficher_solde()
Compte2.afficher_solde()
Compte1.afficher_solde()

