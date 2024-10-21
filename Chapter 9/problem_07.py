'''
Question:- Write a program to find out the line number where python is present
from ques 6

'''

with open("file3.txt", "r") as f:
    lines = f.readlines() # this function will read each and every line and store it into lines in the form of file

lineno=1
for line in lines:
    if("python" in line):
        print(f"The word python is present in the line:- {lineno}")
        break
    lineno+=1

else:
    print("The word python is not present")