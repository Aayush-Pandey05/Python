#Question:- print the following pattern:- 
'''
*   there are two spaces after one star therefore no. of stars = i
**  and no. of spaces = n-i
***
'''

n=int(input("Number of rows:- ")) 

for i in range (1, n+1):
    print("*"*i, end="")
    print(" "*(n-i), end="")
    print("")