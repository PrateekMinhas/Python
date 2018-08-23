#Q.1- Create a function to calculate the area of a sphere by taking radius from user.
r=int(input("enter radius"))
pi=3.14
def area(rad):
    a=4*pi*rad*rad
    return(a)
ar=area(r)
print(ar)

#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program
#that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].



def perfect(m):
    s=0
    for i in range (1,m):
        if m%i==0:
            s=s+i
    return(s)

       

            

for x in range (1,1000):
    
    per=perfect(x)
    if per==x:
        print(x)


#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user. 

n=int(input("enter num"))

for i in range (1,11):
    print(str(n)+' *  %d = %d'%(i,i*n))



#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
a=int(input("enter number"))
b=int(input("enter power raised to"))
def power(c,d):
    if d!=0:
        return(c* power(c,d-1))
    else:
        return 1
    





res=power(a,b)
print(res)
