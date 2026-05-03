#two child derived from one parent but have different properties
class A:                                     #parent
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):                                  #child of A
    a,b=30,20
    def m2(self):
        print(self.a*self.b)
class C(A):                                  #child of A
    m,n=250,125
    def m3(self):
        print(self.m-self.n)
obj=B()
obj.m1()
obj.m2()
obj=C()
obj.m1()
obj.m3()