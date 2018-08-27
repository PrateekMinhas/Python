#Q.1- Name and handle the exception occured in the following program: 

'''a=3
     if a<4:
        a=a/(a-3)
         print(a)'''

a=3
if a<4:
    try:
        a=a/(a-3)
    except:
        print ("zero division error occured here")


#Q.2- Name and handle the exception occurred in the following program: 
#l=[1,2,3] 
#print(l[3])

l=[1,2,3]
try:
    print(l[3])
except:
    print("index error here occured")


#Q.3- What will be the output of the following code:

    # Program to depict Raising Exception
     
'''try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not'''
#An exception
#NameError





#Q.4- What will be the output of the following code: 

     # Function which returns a/b
'''def AbyB(a , b):
        try:
            c = ((a+b) / (a-b))
        except ZeroDivisionError:
            print("a/b result in 0")
        else:
            print(c)
    
    # Driver program to test above function
    AbyB(2.0, 3.0)
    AbyB(3.0, 3.0)'''

#-5
#a/b result in 0



#Q.5- Write a program to show and handle following exceptions: 
#1. Import Error 
#2. Value Error 
#3. Index Error 

#1 import Error

lis=[1,2,3,[4,5],33]
try:
    lis1=copy.deepcopy(lis)
except:
    print("something is not imported")

#2 Value Error

try:
    x=int(input("enter number"))
except ValueError :
    print("enter an integer")


#3 Index Error
lis3=[1,2,3,4,5]
try:
    y=lis3[7]
except IndexError :
    print("give propper index")
    

    




    
    
    




    
