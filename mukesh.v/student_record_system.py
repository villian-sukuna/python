FILENAME = "student.txt"
# Add Student
def add_student():
    try:
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        sid = input("Enter Student ID: ")

        with open(FILENAME, "a") as file:
            file.write(f"{name},{age},{sid}\n")

        print("Student record added successfully!")

    except Exception as e:  
        print("Error:", e)


# Display All Students
def display_students():
    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()

            if len(records) == 0:
                print("No records found.")
            else:
                print("\nStudent Records")
                for line in records:
                    name, age, sid = line.strip().split(",")
                    print("Name :", name)
                    print("Age  :", age)
                    print("ID   :", sid)
                    print("")

    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("Error:", e)


# Search Student by ID
def search_student():
    try:
        search_id = input("Enter Student ID: ")

        with open(FILENAME, "r") as file:
            found = False

            for line in file:
                name, age, sid = line.strip().split(",")

                if sid == search_id:
                    print("\nStudent Found")
                    print("Name :", name)
                    print("Age  :", age)
                    print("ID   :", sid)
                    found = True
                    break

            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("Error:", e)


# Append New Student
def append_student():
    add_student()


# Delete Student by ID
def delete_student():
    try:
        delete_id = input("Enter Student ID to delete: ")

        with open(FILENAME, "r") as file:
            records = file.readlines()

        with open(FILENAME, "w") as file:
            found = False
            for line in records:
                name, age, sid = line.strip().split(",")

                if sid != delete_id:
                    file.write(line)
                else:
                    found = True

        if found:
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")

    except FileNotFoundError:
        print("Student file not found.")
    except Exception as e:
        print("Error:", e)


# Menu
while True:

    choice = input("""    ===== Student Record System =====
    1. Add Student
    2. Display Students
    3. Search Student by ID
    4. Append Student
    5. Delete Student
    6. Exit
    Enter your choice: """)
    match choice:
        case "1":
            add_student()
        case "2":
            display_students()
        case "3":
            search_student()
        case "4":
            append_student()
        case "5":
            delete_student()
        case "6":
            print("Thank You!")
            break
        case _:
            print("Invalid Choice!")