#Question:- Use a reccursive function to print the sum of first n natural numbers:-

def Sum(n):
    if(n==1): 
        return 1
    return n + Sum(n-1) 

n = int(input("Enter the nth natural number:- "))
a = Sum(n) 
print(a)