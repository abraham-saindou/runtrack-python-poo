class Student:
    def __init__(self, nom, prenom, numero):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credit = 0
        self.__level = self.__studentEval()

    def add_credits(self, num):
        if num > 0:
            self.__credit = self.__credit + num
            print(f"Le nombre de crédit de {self.__nom} {self.__prenom} est de {self.__credit} points.")
        return self.__credit

    def __studentEval(self):
        self.add_credits(40)  # Call adding function 3 times
        self.add_credits(30)
        self.add_credits(60)
        if self.__credit < 60:
            reward = "Insuffisant"
        if self.__credit >= 60:
            reward = "Passable"
        if self.__credit >= 70:
            reward = "Bien"
        if self.__credit >= 80:
            reward = "Très Bien"
        if self.__credit >= 90:
            reward = "Excellent"
        return reward

    def studentInfo(self):
        print(f"\nNom et prénom : {self.__nom}, {self.__prenom}\nNuméro étudiant : {self.__numero}")
        print(f"Crédits : {self.__credit} \nNiveau : {self.__level}")


etu1 = Student("John", "Doe", 145)
etu1.studentInfo()
