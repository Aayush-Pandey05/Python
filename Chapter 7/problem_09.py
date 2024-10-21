#Question:- Print the following pattern:- 
'''
* * * *
*     *  there are (n-2) spaces 
*     *  
* * * *
'''

n = int(input("Enter the number of rows:- "))
for i in range (1, n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")