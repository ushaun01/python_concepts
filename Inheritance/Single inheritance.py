`#1:
class A:                                                   #parent class
    def m1(self):
        print("hello")
class B(A):                                                 #child class of parent class A
    def m2(self):
        print("hey")

obj=B()
obj.m1()
obj.m2()

#2:
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
obj=B()
obj.m1()
obj.m2()

#3:
class ABC:
    def add(self):
        print("method 1")
class AB(ABC):
    def sub(self):
        print("method 2")
obj=AB()
obj.add()
