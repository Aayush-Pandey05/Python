# Question:- Write a function to find the greatest from 3 numbers:- 

def greatest(a , b, c):
    if(a>b and a>c):
        print(f"{a} is the greatest number")
    elif(b>a and b>c):
        print(f"{b} is the greatest number")
    else:
        print(f"{c} is the greatest number")

a = int(input("Enter the first number:- "))
b = int(input("Enter the second number:- "))
c = int(input("Enter the third number:- "))
greatest(a , b, c)