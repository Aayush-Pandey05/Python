# Question:- Take the input of eight numbers and print them without repeatation 

# we will make use of SETS to print the numbers without any repetation because repetition is not allowed in sets 

n_1 = int(input("Enter the first number:- "))
n_2 = int(input("Enter the second number:- "))
n_3 = int(input("Enter the third number:- "))
n_4 = int(input("Enter the fourth number:- "))
n_5 = int(input("Enter the fifth number:- "))
n_6 = int(input("Enter the sixth number:- "))
n_7 = int(input("Enter the seventh number:- "))
n_8 = int(input("Enter the eighth number:- "))

set = {n_1,n_2,n_3,n_4,n_5,n_6,n_7,n_8}

print(set)

#SETS doesnot follow any order and we cant access its elements through indexes therefore the values cant be altered 
