class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * self.TVA
        return prixTTC

    def modifier(self, nom, prixHT):
        self.nom = nom
        self.prixHT = prixHT

    def afficher(self):
        TTCproduit = str(self.CalculerPrixTTC())
        strTVA = str(self.TVA)
        word1 = "Nom de l'article : " + self.nom
        word2 = "\nPrix HT de l'article en € : " + str(self.prixHT)
        word3 = "\nPrix total de l'article en €: " + TTCproduit
        word4 = "\nTVA de l'article en €: " + strTVA + '\n'
        phrase = word1 + word2 + word3 + word4
        print(phrase)

produit1 = Produit("Poulet", 5, 1.2)
produit1.afficher()
produit2 = Produit("Patate", 1, 1.2)
produit2.afficher()
produit2.modifier("Savon", 2.3)
produit2.afficher()
