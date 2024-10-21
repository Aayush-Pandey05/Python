'''
Question:- Write a class “Calculator” capable of finding square, cube and square root of a 
number

'''

class calculator:
    def __init__(self, n):
        self.n =n

    def square(self):
        print(f"the square of the number is {self.n*self.n}")
    def cube(self):
        print(f"the cube of the number is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"the root of the number is {self.n**1/2}") # ** signifies power
    
n1 = calculator(4)
n1.square()
n1.cube()
n1.squareRoot()

        