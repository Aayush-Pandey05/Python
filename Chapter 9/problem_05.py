'''
Question:- Repeat program 4 for a list of such words to be censored.

'''

words = ["ganda", "Donkey", "chamar", "lodu"] #list of bad words that are needed to be censored 

with open ("file2.txt", "r") as f: # reading the content of the file 
    content = f.read()

for word in words: # replacing every bad word int the list 
    content = content.replace(word, "#"*len(word))

with open("file2.txt", "w") as f: # printing the replaced words in the text file 
    f.write(content)