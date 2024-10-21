#Question:- Develop a function to convert celcius to ferhenite
'''
 F= (9/5*C)+32
'''
def convert(c):
    f = (9/5*c)+32
    print(f"The ferhenite temperature is {f}")

c = int(input("Enter the temperature in celcius:- "))
convert(c)