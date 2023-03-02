class Task:
    def __init__(self, nom, description, status):
        self.nom = nom
        self.description = description
        self.status = status

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        t = [task.nom, task.description, task.status]
        self.tasks.append(t)

    def del_task(self):
        pass
        # liste = []
        # print(self.tasks)
        # for obj in self.tasks:
        #     liste.append(obj.keys())
        # input(f"Which object do you want to delete ? {liste[0]} or {liste[1]} or {liste[2]}")
        #
        # print(liste)

    def mark_asdone(self):
        self.tasks[0][2] = True

    def show_list(self):
        print(f"Task 1 : {self.tasks[0][0]}, {self.tasks[0][1]}, and status is {self.tasks[0][2]}")
        print(f"Task 2 : {self.tasks[1][0]}, {self.tasks[1][1]}, and status is {self.tasks[1][2]}")
        print(f"Task 2 : {self.tasks[2][0]}, {self.tasks[2][1]}, and status is {self.tasks[2][2]}")
    def filter_list(self):
        pass


Tlist = TaskList()
Tlist.add_task(Task("Walk", "Walk a full mile", False))
Tlist.add_task(Task("Eat", "At the restaurant", False))
Tlist.add_task(Task("Sleep", "At home", False))
Tlist.show_list()
Tlist.mark_asdone()
Tlist.show_list()
