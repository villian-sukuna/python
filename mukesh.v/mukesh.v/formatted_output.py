name = input("Enter Your name:")#used input to gvet input from user
age=int(input("enter your age:"))
mark=int(input("enter your mark"))
print(f"My Name is {name} and my age is {age}")#formateed the output here
if mark>=40:
    result=True
    print("pass")
   
else:
    result=False
    print("fail")
print(type(result))

