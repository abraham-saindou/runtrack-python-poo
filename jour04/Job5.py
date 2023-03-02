import math
class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        aire = self.longueur * self.largeur
        print(f"L'aire du rectangle est de {aire} cm2.")


class Cercle(Forme):
    def __init__(self, radius):
        self.radius =  radius

    def aire(self):
        aire = self.radius * self.radius * math.pi
        print(f"L'aire du cercle de {self.radius} cm rayon est de {aire} cm2.")


rect1 = Rectangle(5, 4)
rect1.aire()
cercle1 = Cercle(3)
cercle1.aire()