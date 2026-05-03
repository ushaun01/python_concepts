#print number from 10-15 using while loop
i=10
while i<=15:
    print(i)
    i=i+1

#print 1-5 number using for loop
for i in range(1,6):
    print(i)

#print 10-1 using while loop
i=10
while i>=1:
    print(i)
    i=i-1

#print addition of first 5 numbers using while loop
a=1
add=0
while a<=5:
    add=add+a
    a=a+1
print(add)
#print addition of first 5 numbers using for loop
add=0
for i in range(1,6):
    add=add+i
print(add)


#print addition of list elements using for loop
add=0
a=[10,30,45,-10]
for i in a:
    add=add+i
print(add)

#print number 1-10 which is divisible by 3
for i in range (1,11):
    if i%3==0:
        print(i)

#print number from 1-10 which is divisible by 2 and 5
for i in range(1,11):
    if i%2==0 and i%5==0:
        print(i)