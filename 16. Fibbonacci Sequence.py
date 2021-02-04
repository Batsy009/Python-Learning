# 16. Fibonacci Sequence.
ran = int(input("Enter the Range of the Sequence : "))
a=0
b=1
c=0

if(ran<=0):
    print("\n Please enter Positive Integer!!\n")
elif(ran==1):
    print("\nThe Fibnacci Sequence upto ", ran, "is :", a)
else :
    print("\nThe Fibonacci Sequence upto", ran, "is :\n")
    while(c<ran):
        
        print(a)
        x=a+b
        a=b
        b=x
        c+=1
      
print()
