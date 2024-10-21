#Question:- Write a program top find the sum of first n natural numbers using while loop

n = int(input("Enter the number:- "))
sum = 0
i = 1
while(i<=n):
    sum = sum + i
    i+=1
print(f"The sum of {n} natural numbers is:- {sum}")