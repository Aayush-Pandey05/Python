#Question:- print the following:- 
'''
  *    it starts with one star and two spaces 
 ***     odd number of stars are being printed, therefore we will use (2n-1)
*****  here n=3 

'''

n = int(input("Enter the number of rows:- "))
for i in range (1, n+1):
    print(" "*(n-i), end="")
    print ("*"*(2*i-1), end="") # end="" function prevents print function to go to next line
    print("") # this print function is necessary to go to the next line after printing the stars