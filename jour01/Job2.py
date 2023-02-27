class Operation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def show(self):
        print("Le nombre affiché est : ", self.num1)
        print("Le nombre affiché est : ", self.num2)


Ope = Operation(2, 3)
Ope.show()

