class Animal:
    def __init__(self):
        self.prenom = None
        self.age = 0
        print(f"L'age de l'animal est {self.age} ans. ")

    def vieillir(self):
        self.age += 1
        print(f"L'age de l'animal est {self.age} ans. ")

    def nommer(self, prenom):
        self.prenom = prenom
        print(f"L'animal se nomme : {self.prenom}.")


Lion = Animal()
Lion.vieillir()
Lion.nommer("Nemelios")

