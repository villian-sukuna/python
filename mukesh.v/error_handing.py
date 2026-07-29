try:
    a = int(input("Num : "))
    b = int(input("Num : "))
    c = a/b
    print(c)

except ZeroDivisionError:
    print("jk")

except ValueError:
    print("hj")

else:
    print("else")

finally:
    print("Sucess")