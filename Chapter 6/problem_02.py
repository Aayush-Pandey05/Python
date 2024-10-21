# Question:- Write a programme to find the greatest of four integers entered by the user

first_n = int(input("Enter the first number:- "))
second_n = int(input("Enter the second number:- "))
third_n = int(input("Enter the third number:- "))
fourth_n = int(input("Enter the fourth number:- "))

# We will be using elif ladder to solve this problem

if(first_n>second_n and first_n>third_n and first_n>fourth_n):
    print(f"The greatest number is:- {first_n}")

elif(second_n>first_n and second_n>third_n and second_n>fourth_n):
    print(f"the greatest number is:- {second_n}")

elif(third_n>first_n and third_n>second_n and third_n>fourth_n):
    print(f"the greates number is:- {third_n}")

else:
    print(f"greatest number is:- {fourth_n}")
