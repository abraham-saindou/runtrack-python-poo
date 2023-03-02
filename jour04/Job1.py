class Person:
    def __init__(self):
        self.age = 14

    def display_age(self):
        print(f"My age is {self.age}.")

    def hello(self):
        print('Hello')

    def modify_age(self, age):
        self.age = age


class Student(Person):
    def gotoschool(self):
        print("I'm going to school.")

class Teacher(Person):
    def __init__(self):
        self.__subject = "Math"

    def teaching(self):
        print("Lesson will begin, take place.")

pers1 = Person()
pers1.modify_age(24)
pers1.display_age()

Student1 = Student()
Student1.hello()
Student1.display_age()
Student1.gotoschool()

teacher = Teacher()
teacher.teaching()
