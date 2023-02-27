import math
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayons(self):
        self.rayon = 4

    def afficherInfos(self):
        pass
    def circonference(self):
        pass
    def aire(self):
        area = self.rayon * self.rayon * math.pi
        print(f"L'aire du cercle est de {area} cm.")

    def diametre(self):
        diametre = self.rayon * 2
        return diametre
Cercle1 = Cercle(3)
Cercle1.aire()