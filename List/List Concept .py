#accesssing items from list
a=[1,2,"usha",4]
print(a[0])
print(a[2])
print(a[-1])   #negative indexing

#range of index
b=[12,34,56,6,78,8,6,4,88]
print(b[2:5])
print(b[-4:-1])

#change items value
c=["usha","anaye","rose",23]
c[1]="orange"
print(c)

#read items using loop
c=["usha","anaye","rose",23]
for i in c:
    print(i)

#check if items exist in the list
c=["usha","anaye","rose",23]
if "anaye" in c:
    print("present")
else:
    print("absent")

#lenth of list
c=["usha","anaye","rose",23]
print(len(c))

#add values in list
m= ["rushi", "usha", "anaye", "rose", 23]
m.append("sun")
m.insert(3,"bhavi")
print(m)

#remove values from list
m= ["rushi", "usha", "anaye", "rose", 23]
m.pop(1)
print(m)
del m[2]
print(m)
m.clear()
print(m)

#copy list
m= ["rushi", "usha", "anaye", "rose", 23]
n=list(m)
print(n)
n=m.copy()
print(n)

#negative indexing
a=[10,20,3,25,5,2]
print(a[-1])

#slicing
a=[10,20,3,5,"apple"]
print(a[1:4])
print(a[1:])

#reverse slicing
a=[10,1,5,6,8,5,9,8]
print(a[::-1])

#ordered reversing
a.sort(reverse=True)
print(a)

#reverse string
a="ashish bajaj"
rev=""
for i in a:
    rev=i+rev
print(rev)

#combine/join list
m= ["rushi", "usha", "anaye", "rose", 23]
n=[1,25,5,3,4]
o=m+n     #concatenation
print(o)
for i in n:
    m.append(i)
print(m)

#extend list
m= ["rushi", "usha", "anaye", "rose", 23]
n=[1,2,56,35,45]
m.extend(n)
print(m)

#sorting
a=[9,0,2,4,56,5,6]
a.sort()
print(a)

#find second-highest element from list
a=[1,25,35,89,2,5,4]
a.sort(reverse=True)
print(a[1])

#Replace value from list
a=[20,30,"mili"]
a[1]=100
print(a)