class Personnage:
    def __init__(self, x, y):
        self.pos_x, self.pos_y = x, y
        self.matrix = [[1, 2, 3], [4, 5, 6], [7, 9, 9]]
        self.player = [self.matrix[0], self.matrix[0][0]]

    def gauche(self):
        self.player

    def droite(self):
        pass

    def haut(self):
        pass

    def bas(self):
        pass

    def position(self):
        pass

Perso1 = Personnage(0, 0)
Perso1.matrix()
