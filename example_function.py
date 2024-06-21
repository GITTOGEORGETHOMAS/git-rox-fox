 
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

a = 9
b = 8
calculateGmean(a,b)

c= 8
d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c,d)

def greet():
    print("Hello, World!")

greet()


def  greet1(name):
    print("Hello, " + name + "!")

greet1("Alice")


def greet2(name = "World"):
    print("Hello, " + name + "!")

greet2() 
greet2("Gitto")  

def add(a,b):
    print(a+b)

add(3,4)
def check(a,b):
    if(a>b):
        print("first number is greater than second number")
    else:
        print("Second number is greater or equal")

def checklesser(a,b):
    pass


num1 = 9
num2 = 18
# if(num1>num2):
#     print("num1 is greater than num2")
# else:
#     print("Second number is greater or equal")
check(num1,num2)


num3 = 97
num4 = 87
# if(num3>num4):
#     print("num3 is greater than num4")
# else:
#     print("num4 is greater than num3")
check(num3,num4)
checklesser(num3,num4)

