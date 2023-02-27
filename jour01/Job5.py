class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def afficherlespoints(self):
        print(f"Les coordonnées x et y du point sont : {self.x} et {self.y}.")

    def afficherX(self):
        print(f"x = {self.x}")

    def afficherY(self):
        print(f"y = {self.y}")

    def changeX(self):
        self.x = 5
        print(f"x = {self.x}")

    def changeY(self):
        self.y = 12
        print(f"x = {self.y}")

Pi = Point(3, 6)
Pi.afficherlespoints()
Pi.afficherX()
Pi.afficherY()
Pi.changeX()
Pi.changeY()