'''
Question:- Write a program to print third, fifth and seventh element from a list using enumerate 
function.

'''
l = [1, 2, 3, 4, 5, 6, 7]

for i , item in enumerate(l):# this is the use(basic syntax)of enumerate function
# Here i refers to the index of the list and item is the items in that list    
    if(i==2 or i==4 or i==5):
        print(item)