'''
Question:- Write a program to filter a list of numbers which are divisible by 5.

'''

def Divisible5(n):
    if(n%5==0):
        return True
    return False

a = [1, 5, 345, 70, 45664,67, 24, 43]
f = list(filter(Divisible5, a)) #this will filter the the above mentioned list and give you the elements which are divisible by 5
# It will happen because in the function we have given the condition that only if the number is divisible by 5 it will return true as the answer
# here we are giving the list as the input in the function and we are getting a list in return
print(f)
