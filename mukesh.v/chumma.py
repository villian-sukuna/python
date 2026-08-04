import os

# 1 & 2. Create class Person with constructor and display method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# 3 & 4. Create class Student that inherits Person with additional variables and file methods
class Student(Person):
    def __init__(self, name, age, st_id, course, marks):
        super().__init__(name, age)
        self.st_id = st_id
        self.course = course
        self.marks = marks

    def display_stud(self):
        self.display_person()
        print(f"Student ID: {self.st_id}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

    def save_stud(self, filename="stud.txt"):
        # Format record as: st_id,name,age,course,marks
        record = f"{self.st_id},{self.name},{self.age},{self.course},{self.marks}\n"
        with open(filename, "a") as file:
            file.write(record)


# File Handling Helper Functions
def view_all_students(filename="stud.txt"):
    try:
        if not os.path.exists(filename) or os.stat(filename).st_size == 0:
            print("\nNo student records found.")
            return

        with open(filename, "r") as file:
            print("\n--- Student Records ---")
            for line in file:
                st_id, name, age, course, marks = line.strip().split(",")
                print(f"ID: {st_id} | Name: {name} | Age: {age} | Course: {course} | Marks: {marks}")
            print("-----------------------")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def search_student_by_id(st_id_to_search, filename="stud.txt"):
    try:
        found = False
        with open(filename, "r") as file:
            for line in file:
                st_id, name, age, course, marks = line.strip().split(",")
                if st_id == st_id_to_search:
                    print("\n--- Student Found ---")
                    student = Student(name, age, st_id, course, marks)
                    student.display_stud()
                    print("---------------------")
                    found = True
                    break
        if not found:
            print(f"\nStudent with ID '{st_id_to_search}' not found.")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def delete_student_by_id(st_id_to_delete, filename="stud.txt"):
    try:
        if not os.path.exists(filename):
            print(f"Error: The file '{filename}' does not exist.")
            return

        lines_to_keep = []
        found = False

        with open(filename, "r") as file:
            for line in file:
                st_id, _, _, _, _ = line.strip().split(",")
                if st_id == st_id_to_delete:
                    found = True
                else:
                    lines_to_keep.append(line)

        if found:
            with open(filename, "w") as file:
                file.writelines(lines_to_keep)
            print(f"\nStudent with ID '{st_id_to_delete}' successfully deleted.")
        else:
            print(f"\nStudent with ID '{st_id_to_delete}' not found.")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# 5. Menu-driven program using a while loop with Exception Handling
def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by ID")
        print("4. Delete Student by ID")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            # Handle invalid menu choices
            if choice not in ['1', '2', '3', '4', '5']:
                raise ValueError("Invalid menu choice! Please select an option between 1 and 5.")

            if choice == '1':
                print("\n--- Add New Student ---")
                st_id = input("Enter Student ID: ").strip()
                name = input("Enter Name: ").strip()
                age = input("Enter Age: ").strip()
                course = input("Enter Course: ").strip()
                marks_input = input("Enter Marks: ").strip()
                
                # Exception Handling: Check if marks are numeric
                if not marks_input.replace('.', '', 1).isdigit():
                    raise TypeError("Invalid input: Marks must be numeric values.")
                
                # Save student to file
                student = Student(name, age, st_id, course, marks_input)
                student.save_stud()
                print("Student details saved successfully.")

            elif choice == '2':
                view_all_students()

            elif choice == '3':
                search_id = input("\nEnter Student ID to search: ").strip()
                search_student_by_id(search_id)

            elif choice == '4':
                del_id = input("\nEnter Student ID to delete: ").strip()
                delete_student_by_id(del_id)

            elif choice == '5':
                print("\nExiting System. Goodbye!")
                break

        # Catch specific custom/value errors raised in execution
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except TypeError as te:
            print(f"Data Type Error: {te}")
        # Catch unexpected errors using except Exception as e
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()