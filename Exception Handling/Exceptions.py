#1:
print("usha")
try:
    print(x)
except:
    print("exception occur")
print("nazare")

#2:Zero division exception
print("starting point")
print("program in process")
try:
    print(10/0)
except ZeroDivisionError:
    print("Exception occurred  ..handled")
print("program completed")

#3: multiple except blocks    try,except,else,finally
try:
    a,b=10,2
    c=a/b
    print("result is",c)
    m,n=1/0
    o=m/n
    print(o)
except ZeroDivisionError:
    print("Zero error")
except SyntaxError:
    print("syntax error")
except:
    print("handled")
else:
    print("no exceptions")
finally:
    print("always executed")

#4: raising our own exceptions
def x(num):
    if num<0:
        raise ValueError("only integers")
    if num%2==0:
        print("even")
    else:
        print("odd")
num=-1
try:
    x(num)
except ValueError:
    print("value error exception")
x(10)
x(5)
