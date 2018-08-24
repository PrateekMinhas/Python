#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.
a={} #initialising an empty dictionary
n=int(input("enter size of dictionary"))

for i in range (0,n):
    key=input("enter key")
    value=input("enter value")
    a[key]= value #since i knows a is a dictionary , therefore it will not take [] as an index but rather 'key' of a dictioanary 
print(a)






#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of
#every student.Print the marks of a given student from that dictionary for every subject. 
#Hint: Use nested dictionary to store subjects marks.
#normal method
stu={'Prateek':{}, 'Caprice':{}}#creation of a dictionary with student names and values are empty dict so as to make them nested
#assigning values to the inner dictionary for first outer key
stu['Prateek']['physics']=99
stu['Prateek']['chem']=98
stu['Prateek']['maths']=97
#assigning values to the inner dictionary for second outer key
stu['Caprice']['physics']=97
stu['Caprice']['chem']=98
stu['Caprice']['maths']=99

print(stu)
#user input method
student={} #initialising an empty dictionary
size=int(input("enter size of dictionary"))

for x in range (0,size):
    k=input("enter name")
    student[k] = {}

    s=int(input("enter number of subjects"))
    for p in range (0,s):
        l=input("enter subject name")
        m=input("enter marks")
        student[k][l]=m
print(student)
