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
        print(f"Lesson of {self.__subject} will begin, take place.")


Student1 = Student()
Student1.hello()
Student1.modify_age(15)
Student1.display_age()
Student1.gotoschool()

teacher = Teacher()
teacher.modify_age(40)
teacher.hello()
teacher.display_age()
teacher.teaching()
