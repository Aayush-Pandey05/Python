'''
Question:- Create a class “Programmer” for storing information of few programmers 
working at Microsoft.

'''

class programmer: # Initializing a class named programmer 
    company = "Microsoft"
    def __init__(self, name, salary, pin):# Constructer initialzation
        self.name = name
        self.salary = salary
        self.pin = pin


p1 = programmer("Aayush", 1200000, 411033) #object of the class programmer
print(p1.company, p1.name, p1.salary, p1.pin)
        
