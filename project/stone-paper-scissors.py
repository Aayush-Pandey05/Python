import random # For generating a random number 


'''

1 for stone 
0 for paper
-1 for scissors

'''

def generate_random_number():
    return random.choice([0, 1, -1]) # This function is returning a random choice between 0, 1 and -1

# Random choice by computer:- 
computer = generate_random_number()


youstr = input("Enter your choice:- ")
youDict = {'stone':1,
           'paper':0,
           'scissors':-1}
you = youDict[youstr]

revDict = {1:'stone', 0: 'paper', -1: 'scissors'}
print(f"Computer chose {revDict[computer]}\nYou chose {revDict[you]}")


if(you==computer):
    print("the game was draw")
if(you==1 and computer==-1): # (-1 - 1 =-2) 
    print("you won")
elif(you==1 and computer==0):# (0 - 1 = -1)
    print("computer won")
elif(you==0 and computer==1):# (1 - 0 = 1)
    print("You won")
elif(you==0 and computer==-1):# (-1 - 0 = -1)
    print("Computer won")
elif(you==-1 and computer==0):# (0 - -1 = 1)
    print("computer won")
elif(you==-1 and computer==1):# (1 - -1 = 2)
    print("you won")
else:
    print("Something went wrong")

'''
If we change the mathematical conditions then we might be able to reduce the 
code by finding some kind of repeated pattern after taking the difference 
between the choices of user and computer and then apply 'if - else' conditional 
statement.....

'''