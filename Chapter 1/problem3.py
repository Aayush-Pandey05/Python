# Question:- write a python program to print the contents of a directory using os module. search online for the function which does that..... 
# we used chatgpt to solve this problem

import os

# Specify the directory path
directory_path = '/'

# List all files and directories in the specified directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
