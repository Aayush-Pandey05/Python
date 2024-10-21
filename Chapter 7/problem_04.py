#Question:- Find out if the number is prime or not 

#prime number:- a number which can only be divivded by one or the number itself

n = int(input("Enter the number :- "))

for i in range (2, n):
    if(n%i==0):
        print("The number is not prime")
        break # if the number is divisible by any number between the given range then it is not a prime number

else:
    print("the number is prime")
        

