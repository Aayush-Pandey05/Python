#Question:- input the marks of 5 students in a list and sort it as well as print it  



stu_marks=[]
s1 = int(input("Enter the marks of the first student:- ")) # we need the marks to be in int as if it is in string then it won't sort the array 
stu_marks.append(s1)
s2 = int(input("Enter the marks of the second student:- "))
stu_marks.append(s2)
s3 = int(input("Enter the marks of the third student:- "))
stu_marks.append(s3)
s4 = int(input("Enter the marks of the fourth student:- "))
stu_marks.append(s4)
s5 = int(input("Enter the marks of the fifth student:- "))
stu_marks.append(s5)

stu_marks.sort() # we can directly make changes in the list as it is mutable unlike strings 
print(stu_marks)
