import os
 
# Person Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name :", self.name)
        print("Age  :", self.age)


# Student Class (Inheritance)
class Student(Person):
    def __init__(self, name, age, st_id, course, marks):
        super().__init__(name, age)
        self.st_id = st_id
        self.course = course
        self.marks = marks

    def display_student(self):
        self.display_person()
        print("ID     :", self.st_id)
        print("Course :", self.course)
        print("Marks  :", self.marks)

    def save_student(self):
        file = open("student.txt", "a")
        file.write(f"{self.st_id},{self.name},{self.age},{self.course},{self.marks}\n")
        file.close()


# View Students
def view_students():
    try:
        file = open("student.txt", "r")

        print("\nStudent Records")
        print("------------------------")

        for line in file:
            data = line.strip().split(",")
            print("ID :", data[0])
            print("Name :", data[1])
            print("Age :", data[2])
            print("Course :", data[3])
            print("Marks :", data[4])
            print("------------------------")

        file.close()

    except FileNotFoundError:
        print("No student records found.")


# Search Student
def search_student():
    sid = input("Enter Student ID : ")

    try:
        file = open("student.txt", "r")
        found = False

        for line in file:
            data = line.strip().split(",")
            if data[0] == sid:
                print("\nStudent Found")
                print("ID :", data[0])
                print("Name :", data[1])
                print("Age :", data[2])
                print("Course :", data[3])
                print("Marks :", data[4])
                found = True
                break

        if not found:
            print("Student not found.")

        file.close()

    except FileNotFoundError:
        print("File not found.")


# Delete Student
def delete_student():
    sid = input("Enter Student ID to delete : ")

    try:
        file = open("student.txt", "r")
        lines = file.readlines()
        file.close()

        file = open("student.txt", "w")
        found = False

        for line in lines:
            data = line.strip().split(",")
            if data[0] != sid:
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("File not found.")


# Main Menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice : ")

    try:
        if choice == "1":
            st_id = input(" Enter ID : ")
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            course = input("Enter Course : ")
            marks = float(input("Enter Marks : "))

            s = Student(name, age, st_id, course, marks)
            s.save_student()

            print("Student Added Successfully.")

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter correct numeric values.")
        
    except Exception as e:
        print("Error :", e)