# 15. Multiplication table
#A. Using While loop

print("\n Using While Loop\n")
n = int(input("\nEnter the Number : "))
i=0
while (i<10):
    i+=1
    t=n*i
    print(n, " x", i, "=", t)
    continue

    
        


#B. Using For loop

print("\n Using For Loop\n")
n = int(input("\nEnter the Number : "))
for i in range(1, 11):
    print(n, " x ", i, "=", n*i)
