'''
Question:- 
Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old.

'''
def generateTable(n): #creating function to print the tables 
    table = "" #this variable will help us to write in the folder 
    for i in range (1, 11): # this range is choosen because we need the tables from 1 to 10
        table+=f"{n} X {i} = {n*i}\n" # We are addingg the strings in the empty  
    with open(f"tables/table_{n}.txt", "w") as f: # this is the syntax to add table of individual numbers in the tables folder
        f.write(table) # now we are writing in the tables  

for i in range(1, 21):
    generateTable(i) # function calling 
    