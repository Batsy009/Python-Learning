# 7. Kilometer to Mile

x = int(input("Enter the unit of distance \n 1. Kilometer \n 2. Miles \n"))
km_to_mile = 0.621371
if(x==1):
    km= float(input("Enter the distance in Kilometers : "))
    mile = km*km_to_mile
    print(km, "KMs = ", round(mile, 2), "Miles")
if(x==2):
    mile = float(input("Enter the distance in Miles : "))
    km = mile/km_to_mile
    print(mile, "Miles = ", round(km, 2), "Kilometers")
