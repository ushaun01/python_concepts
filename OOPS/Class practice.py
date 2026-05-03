#1:
class A:
    def fun(self):
        print("usha")
mob1=A()
mob1.fun()
mob2=A()
mob2.fun()

#2:
class B:
    def ant(self,a):
        print("16gb")
        print(a)
mob1=B()
mob1.ant("Anaye")

#3:
class B:
    def ant(self,a):
        print("16gb")
        print(a)
mob1=B()
mob2=B()
a=10
mob2.ant(a)

#4: create class abcd and print this is method
class ABCD:
    def method(self):
        print("This is method")
obj=ABCD()
obj.method()

#5: Default Constructor:no need to call object
class AB():
    def __init__(self):
        print("usha")
obj=AB()

#6: parameterised constructor
class A:
    def __init__(self,a,b):
        print(a)
        print(b)
obj=A(10,20)

#7:
class A:
    def __init__(self,a=19,b=20):
        print(a)
        print(b)
obj=A()

#8: mixed constructor
class B:
    def __init__(self):
        print("usha")

    def __init__(self,m,n):
        print(m)
        print(n)
object=B(12,25)

#9:
class Abcd:
    def __init__(self):
        print("money")
    def __init__(self,a,b):
        a=b
        print(a)
obj=Abcd(10,20)

#10:
class Abcd:
    def __init__(self):
        print("money")
    def __init__(self,a,b):
        a=b
        print(a)
        b=a
        print(b)
        c=a+b
        print(c)
        self.d=c
        print(self.d)
obj=Abcd(10,20)