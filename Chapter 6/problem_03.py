#  Question:- Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user

mark_1 = int(input("Enter the marks of first subject:- "))
mark_2 = int(input("Enter the marks of first subject:- "))
mark_3 = int(input("Enter the marks of first subject:- "))

total_per = ((mark_1+mark_2+mark_3)/300)*100

if(total_per>=40 and mark_1>=33 and mark_2>=33 and mark_3>=33):
    print('student is passed')

else:
    print('better luck next time')
