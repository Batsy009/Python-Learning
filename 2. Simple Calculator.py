#Program 2 - Simple Calculator

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    if (b==0):
        return("not possible!!")
    else:
        return(a/b)

a = int(input("Enter the first number = "))
b = int(input("Enter the second number = "))
op = input("Enter the Operator : ")
if(op == '+'):
    print("The Addition is ", add(a,b))
elif(op == '-'):
    print("The Substraction is ", sub(a,b))
elif(op == '*'):
    print("The Multiplication is ", mul(a,b))
elif(op == '/'):
    print("The Division is", div(a,b))
else :
    print("Invalid operator")
