"""
def greet(name):
    print("hello,",name)

greet("jb")
greet("magi")

def add(a,b):
    print(a+b)

add(10,5)
add(11,5)

def sub(a,b):
    print(a-b)

sub(10,5)
sub(11,5)


def mul(a,b):
    print(a*b)

mul(10,5)
mul(11,5)


def div(a,b):
    print(a/b)

div(10,5)
div(11,5)



def login(name,password):

    print(f"hello {name} you have logged in ")

name=input("enter your name:")
password=input("enter your password:")
login(name,password)

func=lambda a:a*a
result=func(11)
print(result)

multiple=lambda a,b,c:a*b*c
mul_val=multiple(2,3,4)
print(mul_val)


def string(name):
    print(name.upper())
string("muk")
"""


name="manga"
print(name[::-1])
print(name[0:5])
print(name[0:11:2])
print(name[-1])