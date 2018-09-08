#q1
import pymongo 
client=pymongo.MongoClient()
database=client['students']
collection=database['student']

#q2andq3
x=0
while(x<10):
    try:
        name = input("Enter name: ")     
        marks = int(input('Enter Marks: '))
        if(marks<0 or marks >100):          
            raise ValueError('Invalid marks')
            x=x-1
        else:
            collection.insert_one({'Name':name,'Marks':marks})  
            x=x+1
    except  ValueError as msg:
        print(msg)

#q4
info=collection.find({"Marks":{"$gt":80}}) 
for i in info:
    print(i)
