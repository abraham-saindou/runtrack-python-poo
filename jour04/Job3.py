class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.get_longueur()
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.get_largeur()
        self.__largeur = largeur

    def perimetre(self):
        perimetre = 2 * (self.__longueur + self.__largeur)
        print(f"Le périmètre est de {perimetre} m²")

    def surface(self):
        surface = self.__longueur * self.__largeur
        print(f"La surface est de {surface} m²")


class Parallepipede(Rectangle):
    def __init__(self,  longueur, largeur, hauteur):
        self.__hauteur = hauteur
        Rectangle.__init__(self, longueur, largeur)

    def volume(self):
        volume = Rectangle.get_longueur(self) * Rectangle.get_largeur(self) * self.__hauteur
        print(f"Volume est de {volume} m3")


para = Parallepipede(19, 24, 32)
para.perimetre()
para.surface()
para.volume()
para.set_largeur(13)
para.volume()
