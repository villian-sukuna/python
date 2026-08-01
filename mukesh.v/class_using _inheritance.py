class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("name:",self.name)

class Student(Person):
    def study(self):
        print("student is studying")

class Teacher(Person):
    def teach(self):
        print("teacher is teaching")

class College(Student,Teacher):
    def clg_info(self):
        print("COLLEGE IS PERI")

C=College(name="kk")
C.show()
C.study()
C.teach()
C.clg_info()
