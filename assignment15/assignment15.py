#q1

import sqlite3

con = sqlite3.connect('students.db')

print("Opened database successfully")

con.close()

#Q2

try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = 'create table students(Name varchar(10) primary key,Marks int(3))'
    
    cursor.execute(query)
    
    print('Table created')
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE')
lis = []
x=0
while(x<10):
    try:
        name = input("Enter name: ")
        marks = int(input('Enter Marks: '))
        if(marks<0 or marks >100):
            raise ValueError('Invalid marks')
            x=x-1
        else:
            t = name,marks
            lis.append(t)
            x=x+1
    except  ValueError as message:
        print(message)



#Q3
try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    query = "insert into students(Name, Marks) values(?,?)"
    records = lis
    cursor.executemany(query, records)
    con.commit()
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE')


#Q4
try:
    con = sqlite3.connect('Students.db')
    cursor = con.cursor()
    query = 'select * from students where Marks > 80'
    cursor.execute(query)
    data = cursor.fetchall()
    print("Students who scored greater than 80 :")
    for row in data:
        print('Name: {}'\
             .format(row[0]))
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE')




