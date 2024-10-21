'''
Question:- copy the contents of a file named this.txt in another file

'''

with open("this.txt", "r") as f:
    content = f.read()

with open("thiscopy.txt", "w") as f:
    f.write(content)