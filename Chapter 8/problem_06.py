#Question:- Write a python program to convert inches to cm 

#Answer:- To convert inches to cm just multiply it with 2.54 cm 

def convert(inch):
    cm = inch*2.54
    print(cm)

inch = int(input("Enter the measurement in inches:- "))
convert(inch)