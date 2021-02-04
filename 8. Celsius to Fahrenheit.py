#8. Celsius to Fahrenheit
# 1 F = (Celsius * 1.8) + 32

deg = int(input("\n  Choose to Coversion.\n \n 1. Celsius to Fahrenheit. \n 2. Fahrenheit to Celsius.\n Enter your Choice : "))
if(deg == 1):
    C = float(input("Enter the Temperature is C : "))
    F = (C*1.8)+32
    print(C, "C in Fahrenheit is : ", round(F, 2), "F")
else:
    F = float(input("Enter the Temperature in F : "))
    C = (F-32)/1.8
    print(F, " F in Celsius is :", round(C, 2), "C")
