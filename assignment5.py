#Q.1- Take an input year from user and decide whether it is a leap year or not.
inp=int(input("enter an year"))
if inp % 4 == 0 :
    print("leap year")
else:
    print("not a leap year")


#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
length=int(input("enter the length"))
breadth=int(input("enter the breadth"))
if length==breadth:
    print("it is a square")
else:
    print("its a rectangle")


#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
pers1=int(input("enter the age of first person"))
pers2=int(input("enter the age of second person"))
pers3=int(input("enter the age of third person"))

if pers1>pers2 and pers1>pers3:
    if pers2>pers3:
        print ('oldest is pers1'+str(pers1) +'youngest is pers3'+str(pers3))
    else:
        print ('oldest is pers1'+' '+ str(pers1) +' ''youngest is pers2'+' '+str(pers2))
elif pers2>pers1 and pers2>pers3:
    if pers1>pers3:
        print ('oldest is pers2'+' '+ str(pers2) +'youngest is pers3'+' '+ str(pers3))
    else:
        print ('oldest is pers2'+' '+ str(pers2) +' ''youngest is pers1'+' '+str(pers1))
else :
    
    if pers1>pers2:
        print ('oldest is pers3'+str(pers1) +'youngest is pers2'+str(pers2))
    else:
        print ('oldest is pers3'+' '+ str(pers1) +' ''youngest is pers1'+' '+str(pers1))
#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR".


age=int(input("enter age"))
sex=str(input('enter sex M or F'))
mar_st=str(input("enter martial status Y or N"))
if age<20 or age >60:
    print("ERROR")
elif sex == 'F':
    print("will work in urban areas only")

else:
    if age >=20 and age < 40 :
        print ('you may work anywhere')
    elif age >=40 and age <=60:
        print('will only work in urban areas')


#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose,
#one unit will cost 100. Judge and print total cost for user.
qty=int(input("enter qty."))
p=qty*100
if p>1000:
    dis=p/10
    newcos=p-dis
    print(newcos)

else:
    print(p)



#LOOPS--------------------------------------------
#Q.1- Take 10 integers from user and print it on screen.
ls=[]

for i in range (0,10):
    f=int(input())
    ls.append(f)

l = " ".join(map(str,ls))
print(l)

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while "TRUE":
    print("DIE", end =" ")

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

num=int(input("enter the number, press -1 to stop"))
ls1=[]
while num != -1:
    ls1.append(num)
    num = int (input())

for i in ls1:
    print(i**2, end = " ")


#Q.4- From a list containing ints, strings and floats, make three lists to store them separately
ls2=[1,'hello',20.009,'world',6.9,1,0,5,'mad']
ls3=[]
ls4=[]
ls5=[]
for i in ls2:
    if isinstance(i,int):
        ls3.append(i)
    elif isinstance(i,str):
        ls4.append(i)
    elif isinstance(i,float):
        ls5.append(i)


print ('int list is '+str(ls3))
print ('string list is '+str(ls4))
print ('float list is '+str(ls5))

#Q.5- Using range(1,101), make a list containing only prime numbers.
ls6=[]

for num in range(1,101):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           ls6.append(num)
print(ls6)

#Q.6- Print the following patterns: 
#* 
#** 
#*** 
#****
rows = int (input("enter no.of rows"))
for i in range (1,rows+1):
    print ("* "*i , end ="")
    print("\n")

#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element,
#if found. Iterate over list using for loop. 
   

    
lst=[]
num=int(input("enter number"))
while num != -1:
    lst.append(num)
    num = int (input())
num1=int(input("enter the number to be deleted from the list"))
if num1 in lst:
         lst.remove(num1)
else:
         print("number is not in the list")
print(lst)


    
    
    
    






    











