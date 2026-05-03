#convert list into set
a=[10,25,35,5,9]
b=set(a)
print(b)

#convert into set and print second highest
a=[10,25,35,5,9,3,4]
b=list(set(a))
b.sort(reverse=True)
print(b)
print(b[1])

#
a=[10,10,10,10]
if list(set(a))==[10]:
    print(a)
print(a[1])

#third-highest value
a={1,2,8,6,95,8,5,56,54,6,9,6,2,5,354}
b=list(set(a))
b.sort(reverse=True)
print(b)
print(b[2])
