'''
Question:- . Write a list comprehension to print a list which contains the multiplication table of a 
user entered number.

'''

a = int(input("Enter the number:- "))

table=[a*i for i in range(1,11)] # This is the basic syntax of the list comprehension method 
print(table)