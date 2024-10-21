'''
Question:- Write a program to find the maximum of the numbers in a list using the reduce 
function.

'''

from functools import reduce # We need to import the reduce function
l = [12, 34, 654, 78, 45, 98, 23, 25]
def greater(a , b):
    if(a>b):
        return a
    return b

print(reduce(greater , l)) #this is the use of reduce function 
# they compare 2 elements at a time from the list and return the 
# value according to the function