class Operation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        sum = self.num1 + self.num2
        print("La somme est de : ", sum)


Ope = Operation(2, 3)
Ope.addition()