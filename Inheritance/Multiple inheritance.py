#child acquire properties from two parent
class A:                                     #parent
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B:                                  #child of A
    a,b=30,20
    def m2(self):
        print(self.a*self.b)
class C(A,B):                                  #child of B
    m,n=250,125
    def m3(self):
        print(self.m-self.n)
obj=C()
obj.m1()
obj.m2()
obj.m3()

#2:
class ABC:
    def add(self):
        print("method 1")
class AB:
    def sub(self):
        print("method 2")
class A(ABC,AB):
    def mul(self):
        print("method 3")
obj=A()
obj.add()
obj.sub()
obj.mul()