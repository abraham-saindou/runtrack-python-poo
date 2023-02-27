class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        print(f"Mon nom complet est {self.nom} {self.prenom}")


Personne1 = Personne("Saindou", "Abraham")
Personne1.sePresenter()
Personne2 = Personne("Jack", "Sparrow")
Personne2.sePresenter()