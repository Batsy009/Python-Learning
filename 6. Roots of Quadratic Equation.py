# 6. Find Roots of Quadratic Equation
# ax^2 + bx + c = 0 , where a!=0
import cmath

a = int(input("Enter the Co-effecient a = "))
if (a==0):
    print("a cannot be zero")
else:
    pass
b = int(input("Enter the Co-effecient b = "))
c = int(input("Enter the Co-effecient c = "))

d = (b**2) - (4*a*c)
float(d)
r1 = (-b-cmath.sqrt(d)/(2*a))
r2 = (-b+cmath.sqrt(d)/(2*a))
print(r1)
print(r2)
