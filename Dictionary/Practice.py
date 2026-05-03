#1:
a={10:100,20:200,30:300,40:400}
print(a.keys())
print(a.values())
b=list(a.values())
print(b[1])

#2: find values and values which are divisible by 2
a={10:100,20:299,30:300,40:590,50:999}
print(a.values())
b=a.values()
for i in b:
    if i%2==0:
        print(i)