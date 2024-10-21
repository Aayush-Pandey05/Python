#Question:- Write a programme to find if the given username contains less than 10 charecters or not

fname = input('enter your name:- ')
if(len(fname)<10): # We will make use of len() function
    print('yes the fname contains less than 10 charecters')

else:
    print('the name contains more than 10 charecters ')