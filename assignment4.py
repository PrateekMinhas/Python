#Q.1- Reverse the whole list using list methods.
ls=[1,2,'hello',[4,5],0]
ls.reverse()
print(ls)
ls[1].reverse()#reverses the nested list
print(ls)


#Q.2- Print all the uppercase letters from a string.
str1=str(input("enter a string"))

for i in str1:
    if i >= 'A' and i <= 'Z':
        print(i,end=' ')#used to print in the same line



#Q.3- Split the user input on comma's and store the values in a list as integers.
inp=str(input("enter numeric inputs"))
y=inp.split(',')#converts string to lists
z=[]#empty list
for i in y:
    z.append(int(i))#type casting

print(z)



#Q.4- Check whether a string is palindromic or not.
str2=str(input("enter a string"))
if str2 == str2[::-1]:
    print("pallindromic string")
else:
    print("non pallindromic string")



#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
import copy
ls1=[1,2,3,['hell',3],'inferno']                 
print("ls1 before deep copying")
print(ls1)
ls2=copy.deepcopy(ls1)
ls2[0]=0
ls2[3][1]='dante'
print("ls1 after getting deep copied")
print(ls1)
print("ls2 after changes and deep copying")
print(ls2)
 ''' in shallow copy , no new object of the nested list is formed , so the changes in the nested list part of the coppied list also changes the orignal list'''
 ''' in deep copy , new object of both list and nested lists are formed , so changes in the nested list part of the coppied lists are limited to itself'''





