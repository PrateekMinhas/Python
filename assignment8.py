#Q.1- Create a circle class and initialize it with radius.
#Make two methods getArea and getCircumference inside this class.

class circle:
    def __init__(self,rad):
        self.rad=rad
    
    def circumfrence(self):
        cir=3.14*2*self.rad
        print(cir)
    def area (self):
        ar=3.14*self.rad*self.rad
        print(ar)
r=int(input("enter radius"))
obj= circle(r)
obj.area()
obj.circumfrence()

#Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
#1. Display - It should display all informations of the student. 
#2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.

class student :
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self,ag,mr):
        print("name = " + self.name +" roll number = "+str(self.rno)+ "\n age = " + str(ag) +" marks = "+ str(mr))
    def setAge(self):
        age=int(input("enter age "))
        return age
    def marks(self):
        marks=int(input("enter marks"))
        return marks
    



n=input("enter name of the student")
rn=int(input("enter roll number"))
obj1=student(n,rn)
m=obj1.marks()
a=obj1.setAge()
obj1.display(a,m)


#Q.3- Create a Temprature class and create two methods: 
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temprature:
    def convertFahrenheit(self):
        c=float(input("enter celcius "))
        f=((9/5)*c)+32
        print("{} celcius = {} fahrenheit".format(c,f))
    def covertCelcius(self):
        f=float(input("enter fahrenheit"))
        c=((f-32)*5)/9
        print("{} fahrenheit = {} celcius".format(f,c))


obj3=Temprature()
obj3.convertFahrenheit()
obj3.covertCelcius()

#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details. 
        
class MovieDetails:
    __artistname=""   #blank
    __year=0
    __rating=0
    def Add (self,name,year,rating):
        self.__aristname=name
        self.__year=year
        self.__rating=rating
    def Display (self):
        print("the artist name is ",self.__artistname,"\n release year =",self.__year,"\n rating= ",self.__rating)
obj4=MovieDetails()
name=input("enter artistname")
year=int(input("enter year"))
rating=int(input("enter rating"))
obj4.Add(name,year,rating)
obj4.Display()



#Q.5- Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method.
class animal:
    def animal_attribute(self):
        p='tigers are striped'
        print(p)

class Tiger(animal):
    pass

tig=Tiger()
tig.animal_attribute()



#Q.6- What will be the output of following code. 

    class A:
        def f(self):
            return self.g()

        def g(self):
            return 'A'

    class B(A):
        def g(self):
            return 'B'

    a = A()
    b = B()
    print a.f(), b.f()
    print a.g(), b.g()
#output will be A  B     because of no constructor overloading the last g() will overwrite the prev g() inherited from A into B
    #           A  B

#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.

class shape :
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self,length,breadth):
        if length == breadth:
            print("area of square is {}".format(length*breadth))
        else:
            print("area of rect is {}".format(length*breadth))
        
        
class rectangle(shape):
    pass
    
class square(shape):
    pass

l=int(input("enter length"))
b=int(input("enter breadth"))
sh=shape(l,b)
rect=rectangle(l,b)
sq=square(l,b)
if l==b:
    sq.area(l,b)
else:
    rect.area(l,b)


















