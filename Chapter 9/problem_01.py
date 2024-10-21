# Question:- Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’

f = open("twinkle.txt")
content = f.read() #this will read the text file
if("twinkle" in content):
    print("The word twinkle is present in the text")


else:
    print("The word twinkle is not present in the text")

f.close()# closing the file is a good practice 
