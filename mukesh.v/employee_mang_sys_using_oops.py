class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"the name of the Employee is {self.name} and the age is {self.age}")

class Employee(Person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id=emp_id
        self.salary=salary
    def show(self):
        print(f"Employee Id is {self.emp_id} and the salary is {self.salary}")

obj=Employee("kk",21,1,1000)
obj.display()
obj.show()