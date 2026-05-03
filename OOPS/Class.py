#1: create class and object
class MyClass:                                                #create class
    def func(self):                                           #method 1
        print("usha")
    def display(self):                                        #method 2
        print("john")
M1=MyClass()                                                  #create object
M1.func()                                                     #call method1
M1.display()                                                  #call method2

#2: pass arguments
class MyClass:
    def func(self):
        print("hi")
    def display(self,name):
        print(name)
M1=MyClass()
M1.func()
M1.display("rushi")

#3: instance method          we can call methods through only object
class MyClass:
    def func(self):
        print("usha")
    def display(self):
        print("john")
M1=MyClass()
M1.func()
M1.display()

#4: static method           we can directly call using class, no creation of object
class MyClass:
    def m1(self):
        print("this is instance method")
    @staticmethod
    def m2(num):
        print(num)
mc=MyClass()
mc.m1()                              #instance method: calling method using object name
MyClass.m2(25)                       #static method: calling method using class name

#5: class variables
class MyClass:
    a,b=10,20                        #class variables which are present in class
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)          #call class variable into local using self.variable name
mc=MyClass()
mc.add()
mc.mul()

#6: types of variables
i,j=15,30                                 #global variables
class MyClass:
    a,b=10,20                             #class variables
    def add(self,x,y):                     #x,y are local variables
        print(x+y)                         #call local variables
        print(self.a+self.b)               #call class variables
        print(i+j)                         #call global variables
mc=MyClass()
mc.add(20,30)

#7:same variable names we should use globals
a,b=15,30                                 #global variables
class MyClass:
    a,b=10,20                             #class variables
    def add(self,a,b):                     #x,y are local variables
        print(a+b)                         #call local variables
        print(self.a+self.b)               #call class variables

        print(globals()["a"]+globals()["b"])     #call global variables by using globals()
mc=MyClass()
mc.add(20,30)

#8: one class have multiple object
class MyClass:
    def display(self,name):
        print("display number")
        print(name)
obj1=MyClass()                #object 1
obj1.display("usha")
obj2=MyClass()                #object2
obj2.display("anaye")

#9: Default Constructor    __init__() no need to call object only create object
class MyClass():
    def __init__(self):
        print("this is constructor")

mc=MyClass()                       #constructor is printed automatically .no need to call object

#10: Parameterised Constructor
class Myclass:
    name="rushi"                       #class variable
    def __init__(self,name):
        print(self.name)                #calling class variable
        print(name)
obj1=Myclass("usha")

#11: Create emp class and create constructor will accept three parameters
class Emp:
    def __init__(self,id,name,sal):
        self.id=id                     #converting local variables into class variables
        self.name=name
        self.sal=sal
    def display(self):
        print(self.id,self.name,self.sal)
obj=Emp(101,"usha",50000)
obj.display()
obj2=Emp(102,'rushi',70000)
obj2.display()


