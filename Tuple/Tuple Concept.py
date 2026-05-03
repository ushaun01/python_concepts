#create tuple
from sys import base_prefix

a=("usha",2,5,36)
print(a)

#access values in tuple
a=("usha","anaye",2,5,3)
print(a[2])
print(a[-1])

#range of indexes
a=("usha","anaye",2,"cherry","apple",5,3,34)
print(a[2:5])
print(a[-4:-1])

#changing tuple values    tuple-list(modify)-tuple
a=("usha","anaye",2,"cherry","apple",5,"sun",4)
b=list(a)
b[0]="ram"
b.append(5)
a=tuple(b)
print(a)

#reading tuple values using loop and answer should be in list
a=("usha","anaye",2,"cherry","apple","sun",4)
print(len(a))
b=[]
for i in range(0,len(a)):
    b.append(a[i])
print(b)

# check whether value is present in tuple
a=("usha",5,2,"cherry","apple","sun",4)
if "anaye" in a:
    print("Present")
else:
    print("Absent")

#Length of tuple
a=("usha","anaye",2,"cherry","apple","sun",4)
print(len(a))

#copy tuple
a=("usha","anaye",2,"cherry","apple","sun",4)
b=a
print(b)

#join/combine tuple
a=("usha","anaye",2,"cherry")
b=(1,3,5,3)
c=a+b
print(c)

#
a=("usha","anaye",2,"cherry","apple","sun",4)
b=(1,3,"mango")
if a==b:
    print("equal")
else:
    print("not equal")