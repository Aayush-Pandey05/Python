'''
Question:- Add a static method in problem 2, to greet the user with hello.

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

    @staticmethod #after the use of static method we are not supposed to mention self in the function
    # As we are not acessing any instance attributes
    def Hello():
        print("Hello World")
    
n1 = calculator(4)
n1.Hello()
n1.square()
n1.cube()
n1.squareRoot()
