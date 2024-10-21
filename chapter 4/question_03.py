# Question:- Show that tupple type cant be changed 



marks_stu = (30, 40 ,50 ,60) #as we used '()' here it is a tupple and not a list therefore we canot make changes in it as it is also immutable
print(marks_stu[1])
marks_stu[1] = 0 # here we will get an error as tupple cant be changed 
print(marks_stu[1])