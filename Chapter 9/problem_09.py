'''
Question:- Write a program to find out whether a file is identical & matches the content of 
another file.

'''

with open("this.txt", "r") as f:
    content1 = f.read()

with open("twinkle.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("The files are identicle")

else:
    print("The files are not identicle")

