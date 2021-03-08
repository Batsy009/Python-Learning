class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        
    def calculate(self):
        total = int(sum(scores)/len(scores))
        if 90<=total<=100: return "O"
        elif 80<=total<90: return "E"
        elif 70<=total<80: return "A"
        elif 55<=total<70: return "P"
        elif 40<=total<55: return "D"
        elif total<40 : return "T"
            
        

firstName = input("\nEnter First Name : ")
lastName = input("\nEnter Last Name : ")
idNum = input("\nEnter ID Number : ")
#numScores = int(input()) # not needed for Python
scores = list( map(int, input("Enter Scores sepearated by a whitespace : ").split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
