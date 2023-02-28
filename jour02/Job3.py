class Livre:
    def __init__(self, titre, auteur, pages, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = disponible

    def verify(self):  # Check book status and return its status
        if self.__disponible:
            print("Le bouquin est disponible")
            return True
        else:
            print("Le bouquin n'est plus disponible")
            return False

    def borrow(self):  # Return a bool stating if a book was borrowed
        disponible = self.verify()
        if disponible:
            print("Vous empruntez le livre.\n")
            self.__disponible = False
            self.borrowed = True
        else:
            print("Vous ne pouvez pas emprunter ce livre, il n'est pas disponible.\n")
            return False

    def returnbook(self):  # invokes verify() and stores what the function returns
        if self.borrowed:
            print("Le livre a déjà été emprunter.")
            print("Vous rendez le livre.")
            self.borrowed = False
            self.__disponible = True
        self.verify()

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_pages(self):
        return self.__pages

    def set_titre(self, titre):
        self.get_titre()
        self.__titre = titre

    def set_auteur(self, auteur):
        self.get_auteur()
        self.__auteur = auteur

    def set_pages(self, pages):
        self.get_pages()
        if pages > 0:
            self.__pages = pages
        else:
            print("Le nombre de pages ne peut etre 0 ou inférieur a 0.")

    def show_data(self):
        print(f"Le nom du livre est {self.__titre}, son auteur est {self.__auteur} "
              f"et son nombre de pages est de {self.__pages}.\n")


livre1 = Livre("Les Fleurs du Mal", "Paule Verlaine", 89, True)
livre1.show_data()
livre1.borrow()
livre1.borrow()
livre1.returnbook()
