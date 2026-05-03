#1
a=[10,20,"usha",34]
for i in a:
    print(i)

#2:addition of list items
a=[10,20,30,40]
add=0
for i in a:

    add=add+i
print(add)

#3:mul of list items
a=[14,25,2,5]
mul=1
for i in a:
    mul=mul*i
print(mul)

#4: factorial
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)

#5:add 3,"usha",9 in empty list
a=[]
a.append(3)
a.append("usha")
a.append(9)
print(a)

#6:insert "anaye"in 2 position
a.insert(1,"anaye")
print(a)

#7
a=[10,25,2,3]
for i in a:
    print(i)

#8: To print 1-10 values in list
a=[]
for i in range(1,11):
    a.append(i)
print(a)

#9: print length of list
a=["mili",2,5,"ralt"]
print(len(a))