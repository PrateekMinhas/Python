Q.1- Write a python program to print the cube of each value of a list using list comprehension.
lst=[1,2,3,4,5]
lstc=[i**3 for i in lst]
print(lstc)


#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
lst_pr= [ i for i in range(2,int(input("Enter the end input of the range for the prime numbers"))) if all(i%j!=0 for j in range(2,i)) ] #all returns true if all items in a seq are true
print(lst_pr)



#Q.3- Write the main differences between List Comprehension and Generator Expression.
"""generator expression uses () while list comprehension uses []
list comprehension returns a list that we can iterate and access via index but same is not the case in generator expression"""



#LAMBDA & MAP

#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.


Celsius = [39.2, 36.5, 37.3, 37.8]
far=list(map(lambda i:(i * (9/5)) + 32,Celsius))
print(far)


#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.
lst1=[10,20,30,40,50]
lstsq=list(map(lambda i:i**2,lst1))
print(lstsq)



#FILTER & REDUCE

#Q.1- Filter out all the primes from a list.
lis3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for m in range(2, 18): 
     lis3 = list(filter(lambda x: x == m or x % m and x > 1, lis3))
print(lis3)


#Q.2- Write a python program to multiply all the elements of a list using reduce.

from functools import reduce
lis4 = [1,2,3,4,5,6,7,8,9,10]
mul = reduce(lambda x, y: x*y,lis4)
print(mul)





