
#Q.1- Create a list with user defined inputs.

ls=[]   
x=int(input("enter the number of elements"))
for i in range (x):
    m=input()
    ls.append(m)
print (ls)

#Q.2- Add the following list to above created list: 
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’] 
ls1=['google','apple','facebook','microsoft','tesla']
ls.extend(ls1)
print(ls)


#Q.3 - Count the number of time an object occurs in a list.
ls2=[1,2,3,3,'rabbit',',','$','$',4,7]
x = input("enter an element from the string to know its occurence in it")
print (ls2.count(x))

#Q.4 - create a list with numbers and sort it in ascending order.
ls3=[1,2,45,6,8,4,3,6,8,9,0,8,67,-4]
ls3.sort()
print (ls3)

#Q.5 - Given are two one-dimensional arrays A and B which are sorted in ascending order.
#Write a program to merge them into a single sorted array C that contains every item from
#arrays A and B, in ascending order. [List] 
A=[1,3,4,6,7,-8,-98]
B=[1,4,5,3,6,56,33,23]
C=[12,34,5]
A.sort() #sorts A
B.sort() #sorts B
C.sort() #sorts C
A.extend(B) #adds b to A
C.extend(A) #adds new A to C
C.sort() #sorts the new C
print(C)#prints C

#Q.6 - Count even and odd numbers in that list.
odd=[]
even=[]
for y in C:
    if y%2==0:
        even.append(y)
    else:
        odd.append(y)

print ("even numbers are ",len(even))
print ("odd numbers are ",len(odd))



#TUPLE
#Q.1-Print a tuple in reverse order.
tup=('apple','mango','banana')
rev=reversed(tup)
print(tuple(rev))

#Q.2-Find largest and smallest elements of a tuples.
tup1=(1,2,4,5,6,78,-90)
print(max(tup1))
print(min(tup1))



#STRINGS
#Q.1- Convert a string to uppercase.
string='im so sister shook ryt now !!'
print (string.upper())

#Q.2- Print true if the string contains all numeric characters.
string2=str(input("enter a string"))
print (string2.isdigit())
#Q.3- Replace the word "World" with your name in the string "Hello World".

string3='Hello World'
print(string3.replace('World','Prateek Minhas'))









