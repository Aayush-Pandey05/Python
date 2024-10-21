# Question:- detect double spacce in a string

A = "aayush is  a good boy"
print(A.find("  ")) #.find function will retyurn the index at which the particular part of string lies and if there is no such string then it will return (-1)


#now we will replace the double space with single space 
print(f"The current string with double space is:- {A}")
print(f"The updated string is:- {A.replace("  "," ")}")

#Strings are immutable therefore if we will print the string A it will remain the same
print(A) 

# Whenever we apply any function on string it returns a new string and the original one remains the same 
# However files/arrays are completely flexible