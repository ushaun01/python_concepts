#range function
from sys import base_prefix

print(list(range(10)))
print(list(range(5,10)))
print(list(range(2,15,2)))
print(list(range(10,1,-2)))

#while loop
#print 1...10 if i=1
i=1
while i<=10:
    print(i)
    i=i+1

#print 1-10 in descending order
i=10
while i>=1:
    print(i)
    i=i-1

#print usha 4 times
i=1
while i<=4:
    print("usha")
    i=i+1

#print hi 3 times if i=3
i=3
while i<=5:
    print("hi")
    i=i+1

#addition of 1-10 using while loop
a=1
add=0
while a<=10:
    add=add+a
    a=a+1
print(add)

#for loop
#print 1-5 number using range function
for i in range(1,6):
    print(i)

#print 5-1 in descending order
for i in range(5,0,-1):
    print(i)

#print 21-30 using range(1,11)
for i in range(1,11):
    i=i+20
    print(i)

#print list
a=[10,20,25]
for i in a:
    print(i)

#multiplication of list elements
mul=1
a=[5,10,2,1]
for i in a:
    mul=mul*i
print(mul)

#even numbers
for i in range(1,11):
    if i%2==0:
        print(i)

#odd numbers
for i in range(1,11):
    if i%2!=0:
        print(i)

#addition using for loop
add=0
for i in range(1,11):
    add=add+i
print(add)

#modulo
a=15
b=2
c=a%b
print(c)

#using or
for i in range(1,10):
    if i%2==0 or i%3==0:
        print(i)

