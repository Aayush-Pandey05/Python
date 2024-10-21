# Question:- create a dictionary of hindi words and their english meanings


Hindi = { #we use curly braces to initialize a dictionary 
    'chutiya': 'bastard',
    'kaun': 'who',
    'kya':'what'
}
# dictionary is mutable therefore its values can be altered 
word=input("enter the word whose meaning you desire:- ")

print(Hindi[word])