#1: overide  method name
class A:
    def m1(self):
        print("method 1")
class B(A):
    def m1(self):
        print("method 2")
obj=B()
obj.m1()                          #child class method is executed


#2: print both using super function
class A:
    def m1(self):
        print("method 1")
class B(A):
    def m1(self):
        print("method 2")
        super().m1()                #use of super function
obj=B()
obj.m1()                          #both are printed

#3: override variables
class Parent:
    name="usha"
class Child(Parent):
    name = "anaye"                                  #override variable name
obj=Child()
print(obj.name)

#4:
class A:
    a,b=10,20
class B(A):
    i,j=12,13
    def m(self,x,y):
        print(x,y)                    #local variables
        print(self.i,self.j)          #class variables
        print(self.a,self.b)          #class variables as clas b acquires a properties
obj=B()
obj.m(5,6)

#5:
class ABC:
    def add(self,a,b):
        print(a+b)
class AB(ABC):
    def add(self,a,b):
        print("usha")                #child class method is executed
obj=AB()
obj.add(10,20)

#6: Override Methods
class Bank:
    def interest(self):
        return 0
class XBK(Bank):
    def interest(self):
        return 10
class YBK(Bank):
    def interest(self):
        return 12

obj=XBK()
print(obj.interest())            #child class method is executed
obj2=YBK()
print(obj2.interest())            #child class method is executed0
