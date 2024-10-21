'''
Question:- Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?

'''

class Demo:
    a = 10


b = Demo()
print(b.a) #This will print the original class attribute that is:- 10
b.a = 0 # Here we are setting the attribute=0 for an object b
print(b.a) # now this will print 0
print(Demo.a) # But, the class attribute won't change and it will print 10

