# Question:- print the table of a number using for loop



n = int(input("Enter the number:- "))

print(f"The table of {n} is:- ")

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")