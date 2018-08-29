#Q.1- Write a Python program to read n lines of a file



n = int(input("Enter number of lines"))
f = open('test.txt','r')
for i in range (0,n):
    lines=f.readline()
    print(lines)
    

f.close()



#Q.2- Write a Python program to count the frequency of words in a file.
f=open('test.txt','r')
d=f.read()
words = d.split()
print(words)
l=[]
for i in words:
    if i not in l:
        l.append(i)
        p=words.count(i)
        print ('count of '+i+' = '+ str(p))
    
        



#Q.3- Write a Python program to copy the contents of a file to another file
f2=open('test.txt','r')
f3=open('test1.txt','w') #will create a new file test1 in write mode
d1=f2.read()
f3.write(d1)
f2.close()
f3.close()


#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

with open("test.txt") as f1,open("test2.txt") as f2,open("Comb.txt","w") as fo:
    for o1,o2 in zip(f1,f2):
        fo.write(o1+o2)




#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.



with open('sort.txt','w') as fu:
    for i in range(0,10):
        num = int(input("Enter random number"))
        fu.write('%d' %num) 

with open('sort.txt', 'r') as fu:
    line = fu.readlines()
    for l in line:
        words = l.split()
    r = [int(i) for i in words]
    r.sort()
    str1 = ' '.join(str(e) for e in r)
    fout = open('Final.txt','w')
    fout.write(str1)
    fout.close()



        
        



    






