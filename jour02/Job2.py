class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

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
        if pages > 0:  # Cannot a number of pages below 1
            self.__pages = pages
        else:
            print("Le nombre de pages ne peut etre 0 ou inférieur a 0.")

    def show_data(self):
        print(f"Le nom du livre est {self.__titre}, son auteur est {self.__auteur} "
              f"et son nombre de pages est de {self.__pages}.")

livre1 = Livre("Les Fleurs du Mal", "Verlaine", 89)
livre1.show_data()
livre1.set_titre("L'Iliade")  # Changing title, author and page number
livre1.set_auteur("Homère")
livre1.set_pages(755)
livre1.show_data()
