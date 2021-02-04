# 12. Find the Largest among three numbers.

print(" \n Enter the three numbers. \n")
a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))

if(a>b and a>c):
    print("A = ", a, ",is the greatest number.")
elif(b>b and b>c):
    print("B = ", b, ",is the greatest number.")
else :
    print("C = ", c, ",is the greatest number.")
