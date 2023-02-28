class Rectangle:
    def __init__(self, longueur, largeur):  # Setting constructor
        self.__longueur = longueur
        self.__largeur = largeur
# Getting private variables
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur
# Modifying private variables
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def afficherInfos(self):
        print(f"Le rectangle est de {self.__longueur} cm de longueur et de {self.__largeur} cm de largeur.")

Rect1 = Rectangle(10, 5)
Rect1.afficherInfos()
Rect1.get_longueur()
Rect1.set_longueur(8)
Rect1.get_largeur()
Rect1.set_largeur(3)
Rect1.afficherInfos()
