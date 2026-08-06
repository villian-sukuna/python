name = input("Enter Your name:")#used input to gvet input from user
age=int(input("enter your age:"))#used int because to convert age into integer
dept=input("Enter your departmant:")
mark=float(input("enter your total average:"))
if age <=18:
    print("you are not eligible")
    if mark >=90:
        print("Grade A")
    elif mark >=75 and mark < 90:
        print("Grade B")
    elif mark >=50 and mark <75:
        print("Grade C")
    else:
        print("Fail")

print("choose: 1.cs.ai, 2.cs.ds, 3.cs, 4.bca")
department =int(input("enter your choice:"))
match department:
    case 1:
        print("cs.ai")
    case 2:
        print("cs.ds")
    case 3:
        print("cs")
    case 4:
        print("bca")
    case _:
        print("invalid choice")