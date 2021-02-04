# 18. Sum of Natural Numbers.
#Using Formula

print("\n Using the Formula\n")

n = int(input(" Enter the Number : "))

if (n<0) :
    print("\n Please enter the Positive Integer.\n")
else:
    print("\n The Sum of", n, "Natural Numbers is : ", int((n*(n+1))/2))


#Without using the Formula

print("\n Without using the Formula.\n")

n = int(input(" Enter the Number : "))
sum = 0

if (n<0) :
         print("\n Please enter the Positive Integer.\n")
else :
     while n>0 :
         sum += n
         n -= 1
     print("\n The Sum of", n, "Natural Numbers is : ", sum)
