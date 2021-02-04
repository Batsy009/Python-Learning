#Program 3 - Find Square root
import cmath

ch = int(input("\n 1. Real Number. \n 2. Complex Number. \n Enter the type of input : "))
if(ch == 1):
    n = input("Enter the number : ")
    sqr = float(n)**0.5
    print("Square root of ", n," is : ", sqr)
        
if(ch == 2):
    n = complex(input("Enter the number : "))
    sqr = cmath.sqrt(n)
    print("Square root of", n, "is :", sqr)






    
    
