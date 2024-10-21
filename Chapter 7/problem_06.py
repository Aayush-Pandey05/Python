# Question:- Print factorial of a given number using for loop

# Factorial:- factorial is the multiplication of all the numbers from 1 to the number given
# Example:- (3)factorial is 1X2X3 = 6

n = int(input("Enter the number:- "))
fact = 1

for i in range (1 , n+1):
    fact = fact*i

print(f"Factorial of the given number is:- {fact}")