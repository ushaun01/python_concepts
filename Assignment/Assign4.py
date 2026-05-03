#1: add values in list using append  and print elements which are divisible by 2,25,35,5,8,10,2
a=[]
a.append(2)
a.append(25)
a.append(35)
a.append(5)
a.append(8)
a.append(10)
a.append(2)
print(a)
for i in a:
    if i%2==0:
        print(i)

#2:divisible value should be in list
a=[]
b=[]
a.append(2)
a.append(5)
a.append(98)
a.append(7)
print(a)
for i in a:
    if i%2==0:
        b.append(i)
print(b)

#3: find second-highest number
a=[12,3,89,25,6,46,30]
a.sort(reverse=True)
print(a[1])

#4: find the smallest number in list
b=[1,0,2,5,3,6]
b.sort()
print(b[0])

#5: check "usha" is present in list
a=["try",2,36,"lion"]
if "usha" in a:
    print("Present")
else:
     print("Absent")

#6: Print 3rd highest number in list and print square of each element
a=[]
a.append(1)
a.append(2)
a.append(10)
a.append(4)
a.append(6)
a.sort(reverse=True)
print(a[2])
for i in a:
    i=i*i
    print(i)

#7: a=[10,10,10,10] convert into set and print a[1]
a=[10,10,10,10]
if list(set(a))==[10]:
    print(a)
    print(a[1])