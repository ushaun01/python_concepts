#1: Positional Arguments:based on position it will assign data ,first value to first
def abc(i,j):
    print(i,j)
abc(25,20)

#2: Keyword Arguments: specified data assign to variable
def xyz(a,b):
    print(a,b)
xyz(b=100,a=15)

#3: default parameters
def func(i,j=10):
    print(i,j)
func(5)                        #default j will printed
func(10,30)               #j will print from this

#4:
def n(a,b,c):
    print(a,b,c)
n(10,20,30)           #positional arguments
n(a=10,b=20,c=30)              #keyword arguments
n(10,20,c=30)            #mixed arguments  positional arguments  must come before keyword arguments

#5: function can return multiple values
def y(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(y(25,100))
print(y(12,5))

