import os
def create_file():
    try:
        file_name = get_name()
        if file_name is None:
            return
        file = open(file_name, "x")
    except FileExistsError:
        print("\nALREADY AN FILE EXISTS IN THIS NAME")
    except ValueError as e:
        print("ERROR", e)
    else:
        file.close()
    finally:
        print()


def read_file():
    file_name = get_name()
    if file_name is None:
        return
    try:
        file = open(file_name, "r")
        lines = file.readlines()

        print("file lines\n")
        for line in lines:
            print(line.strip())

    except FileNotFoundError:
        print("ERROR, ENTER PROPER FILE NAME OR FILE SEEMS TO BE MISSING")
    else:
        file.close()
    finally:
        print()


def get_name():
    try:
        name = input("\nENTER FILE NAME : ")
        if name == "":
            raise ValueError("Name cannot be empty")
        return name
    except ValueError as e:
        print("\nFILE NAME ERROR:", e)
        return None


def write_file():
    file_name = get_name()
    lines=[]

    if file_name is None:
        return
    try:
        file = open(file_name, "w")
        print("Enter text to write in file")
        while True:
            text=input()
            if text =="":
                break
            lines.append(text+"\n")
            for line in lines:
                file.write(line)
            print("written successsfully")
    except FileNotFoundError:
        print("FILE NOT FOUND")
    else:
        file.close()
    finally:
        print()


def delete_file():
    file_name = get_name()
    if file_name is None:
        return
    try:
        import os

        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("ENTER PROPER FILE NAME TO DELETE")
    finally:
        print()


while True:
    try:
        print("1.CREATE FILE \n2.READ FILE\n3.WRITE FILE\n4.DELETE FILE")
        option = int(input("ENTER YOUR OPTION (1-4)"))

        match option:
            case 1:
                create_file()
            case 2:
                read_file()
            case 3:
                write_file()
            case 4:
                delete_file()
    except ValueError:
        print("INVALID OPTION, PLEASE ENTER AN NUMBER FROM RANGE 1-4")