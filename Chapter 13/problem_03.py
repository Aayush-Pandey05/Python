'''
Question:- A list contains the multiplication table of 7. write a program to convert it to vertical 
string of same numbers.

'''
# We will make use of 'JOIN' function:- 

table = [str(7*i) for i in range(1,11)] #here we converted 7*i into string because join function only works for strings
a = "\n".join(table) #This is the basic syntax of the join function
print(a) #Printing the veritcal table 

#Join function joins the consecutive strings with whatever we want 
#in this case it was \n