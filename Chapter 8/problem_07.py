'''
Question:- Write a python function to remove a word from the list 
and strip it at the same time 

'''

def remove(l , word ):
    n = [] #We created an empty list to add items to it afterwards 
    for item in l: # This will select every item from the list l
        if(item != word):
            n.append(item.strip(word)) # this will add the items of list l to list n with an stripped off
    return n

l = ["Harry", "Rohan", "an"]
print(remove(l, "an"))