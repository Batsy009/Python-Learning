import re
N = int(input("Enter the number of candidates : ").strip())
lst=[]
for a0 in range(N):
    firstName,emailID = input("Enter the name and Mail-ID sepearates by space : \n").strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search('@gmail\.com$',emailID):
        lst.append(firstName)
print(*sorted(lst),sep='\n')
