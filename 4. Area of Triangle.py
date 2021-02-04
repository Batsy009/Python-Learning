#4. Area of Triangle
print("Enter the length of sides in cms\n")
a = float(input("Enter the side 1 : "))
b = float(input("Enter the side 2 : "))
c = float(input("Enter the side 3 : "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The Area of the triangle is : ", round(area, 2), "sq.cms")
