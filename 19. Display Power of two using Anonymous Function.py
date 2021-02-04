# 19. Display Power of two using Anonymous Function

t = int(input("\n Enter How many terms? \n"))

result = list(map(lambda x : x**2, range(t)))

print("\n The total terms are : ", t)
for i in range(t):
    print("2 raised to Power", i, "is", result[i]S)
