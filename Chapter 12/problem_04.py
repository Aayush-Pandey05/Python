'''
Question:- Write a program to display a/b where a and b are integers. If b=0, display infinite by 
handling the ‘ZeroDivisionError’.

'''

try:
    a = int(input("Enter the first number:- "))
    b = int(input("Enter the second number:- "))
    print(a/b)

except ZeroDivisionError as e:
    print("Infinity")