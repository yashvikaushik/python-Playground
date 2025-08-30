def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b != 0:
        return a / b   # use / for normal division
    else:
        return "Error: Division by zero"
    

ch=input("Enter the symbol for the mathematical operation you want to perform: ")
if(ch=='+'):
    a=int(input("enter number 1: "))
    b=int(input("enter number 2: "))
    print(add(a,b))

elif(ch=='-'):
    a=int(input("enter number 1: "))
    b=int(input("enter number 2: "))
    print(subtract(a,b))

elif(ch=='*'):
    a=int(input("enter number 1: "))
    b=int(input("enter number 2: "))
    print(multiply(a,b))

elif(ch=='/'):
    a=int(input("enter number 1: "))
    b=int(input("enter number 2: "))
    print(divide(a,b))

else:
    print("wrong operator chosen")
