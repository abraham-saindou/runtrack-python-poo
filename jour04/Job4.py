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


rect = Rectangle(12, 4)
rect.aire()