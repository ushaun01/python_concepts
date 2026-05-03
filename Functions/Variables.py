#1:
a=20                                 #global variable(can be before or after function)
def add():
    x=10                             #local variable
    print(x)
    print(a)
add()
print(a)                            #global variable can be accessed outside function also

#2: global and local variable name same, it will return local variable value
xy=100
def abc():
    xy=500
    print(xy)
abc()

#3: change local variable into global variable
xy=100
def e():
    global xy                        #changes local variable into local
    xy=900                           # it is global variable now
    print(xy)
e()
print(xy)                            #900 as it is global variable

#4:
def x():
    global ab
    ab=5                             #it is a global variable
    print(ab)
x()

#5:
x=100
def xyz():
    global x
    x=500
    print(x)

print(x)                             # 100 as we didn't call function

#6:
def m():
    global x                          #we can create global variable inside fun by using global keyword
    x=100
    print(x)
m()
print(x)                             #can be accessed outside as it is global variable

#7: types of variables
i,j=15,30                                 #global variables
class MyClass:
    a,b=10,20                             #class variables
    def add(self,x,y):                     #x,y are local variables
        print(x+y)                         #call local variables
        print(self.a+self.b)               #call class variables
        print(i+j)                         #call global variables
mc=MyClass()
mc.add(20,30)

#8:same variable names we should use globals
a,b=15,30                                 #global variables
class MyClass:
    a,b=10,20                             #class variables
    def add(self,a,b):                     #x,y are local variables
        print(a+b)                         #call local variables
        print(self.a+self.b)               #call class variables

        print(globals()["a"]+globals()["b"])     #call global variables by using globals()
mc=MyClass()
mc.add(20,30)