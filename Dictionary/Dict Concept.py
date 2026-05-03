#create dict
a={"name":"usha x","age":25,"colour":"red"}
print(type(a))

#access elements from dict
a={"name":"usha","age":25,"colour":"red"}
print(a["name"])

#using get()
print(a.get("age"))

#change values in dict
x={"name":"usha x","age":25,"colour":"red","year":2022}
x["name"]="rushi"
print(x)

#reading items in dict using loop
a={"name":"usha","age":25,"colour":"red"}
for i in a:
    print(i)                    #only keys
for i in a:
    print(a[i])                 #only values
for i in a.values():
    print(i)
for i in a.keys():
    print(i)
for i,j in a.items():
    print(i,j)                    #key and value

#check whether key is existing in dict
a={"name":"usha x","age":25,"colour":"red"}
if "name" in a:
    print("present")
else:
    print("absent")

#find total number of items in dict
a={"name":"usha x","age":25,"colour":"red"}
print(len(a))

#add items in dict
a={"name":"usha x","age":25,"colour":"red"}
a["year"]=2021
print(a)

#remove items from dict
a={"name":"usha x","age":25,"colour":"red"}
a.pop("name")
print(a)
a.clear()
print(a)

#copying dict
a={"name":"usha x","age":25,"colour":"red"}
b=a
print(b)
c=a.copy()                          #using copy
print(c)
