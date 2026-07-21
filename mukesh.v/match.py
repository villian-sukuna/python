name=input("enter your name:")
match name:
    case "magi":
        print("pass")

    case "mugi":
        print("fail")
    case "akash":
        print("pass")
    case _:
        print("you are not a student here")