print("Student Profile")
"""GET THE 
STUDENTS INFORMATION 
USING THIS FORM"""
name = input("Enter Your name:")#used input to gvet input from user
age=int(input("enter your age:"))#used int because to convert age into integer
phone=int(input("enter your phone number:"))
dept=input("Enter your departmant:")
height=float(input("enter your height:"))
weight=float(input("enter your weight:"))

next_age=age+1
student_BMI=weight/(height*height)
print(f"your name is {name} and your age is {age} and your phone is {phone} Your department is {dept}")
print("age of you next year:",next_age)
print("student BMI:",student_BMI)