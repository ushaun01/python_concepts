#create set
a={"apple","banana","cherry"}
print(a)

#access values from set
a={"apple","banana","cherry","melon","berry"}
for i in a:
    print(i)

#check values exist in set
a={"grapes","apple","banana","cherry","mango"}
if "melon" in a:
    print("Present")
else:
    print("Absent")
print("banana" in a)

#add values in set
a={"apple","banana","cherry"}
#add-single values  update-multiple values
a.add("orange")
print(a)
a.update(["grapes","berry"])
print(a)

#find length of set
a={"apple","banana","cherry",2,58,3}
print(len(a))

#remove value in set
a={"apple","banana","cherry",2,58,3}
a.remove("banana")
print(a)

#clear all values from set
a={"apple","banana","cherry",2,58,3}
a.clear()
print(a)

#combine two sets
a={"apple","banana","cherry"}
b={1,2,3,52,5}
c=a.union(b)
print(c)

#udate set
a={"apple","banana","cherry"}
b={1,2,3,52,5}
a.update(b)
print(a)
