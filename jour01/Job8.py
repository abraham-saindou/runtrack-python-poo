import math
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayons(self):
        self.rayon = 4

    def afficherInfos(self):
        diametre = self.diametre()
        aire = self.aire()
        circonference = self.circonference()
        print(f"Le rayon du cercle est de {self.rayon} cm, son aire est de {aire} cm, "
              f"sa circonférence est de {circonference} cm et son diametre est de {diametre} cm. ")
        self.changerRayons()
        print(f"Son nouveau rayon est de {self.rayon} cm.")
    def circonference(self):
        diametre = self.diametre()
        circonference = diametre * math.pi
        return circonference
    def aire(self):
        area = self.rayon * self.rayon * math.pi
        return area

    def diametre(self):
        diametre = self.rayon * 2
        return diametre
Cercle1 = Cercle(4)
Cercle2 = Cercle(7)
Cercle1.afficherInfos()
Cercle2.afficherInfos()