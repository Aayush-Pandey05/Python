#Question:- use function to print the following pattern:- 
'''
***   here there are n-i number of stars where n ranges from (0,n)
**
*

'''

def pattern(n):
    for i in range (0, n):
        print("*"*(n-i))

n = int(input("Enter the number of rows:- "))
pattern(n)