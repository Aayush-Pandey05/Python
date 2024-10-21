'''
Question:- 
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hiscore.txt whenever the game() function breaks the Hi-score

'''
import random
def game():# creating a function 
    print("You are playing the game:- ")
    score = random.randint(1,62) #this will generate a random number in between 1 and 62 excluding the number 62
    #Read the highscore:-
    with open('hiscore.txt') as f:
        hiscore = f.read() # reading the text file 
    if(hiscore!=""): # it the text file is having any number then it will be the hiscore
        hiscore=int(hiscore)
    else: # if the text file is empty then highscore will be equal to zero 
        hiscore=0
    
    print(f"your score is {score}")
    if(score>hiscore):   
        #write in the file:
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    
    return score

game()

