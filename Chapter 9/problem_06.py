'''

Question:- Write a program to mine a log file and find out whether it contains
‘python’.

'''
with open("file3.txt", "r") as f:
    content = f.read()
if("python" in content):
    print("Yes python is present in the file")
else:
    print("no python is not present in the file")    
