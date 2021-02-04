# 14. Find the Factorial of a number

def factorial(n):
    if n == 0:
     return 1
    else:
        result = (n*factorial(n-1))
        return result

num = int(input("Enter the Number : "))
fac = factorial(num)
print(fac)
