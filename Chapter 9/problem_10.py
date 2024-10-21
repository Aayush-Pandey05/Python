'''
Questtion:-  Write a program to wipe out the content of a file using python.


Explaination:- write an empty string in any file to make it empty 
'''

with open("thiscopy.txt", "w") as f:
    f.write("")
