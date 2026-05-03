#if else 
a=8
b=10
if a==b:
    print("equal")
else:
    print("not equal")


num=110
if num%2==0:
    print("even number")
else:
    print("odd number")


#in single statement
num=10
print("even number") if num%2==0 else print("odd number")


#blank output
m=10
n=20
if m==n:
    print("equal")


#overwrite value
a=10
b=15
if a==b:
    print("equal")
a=10
b=35
print(a+b)

#if elif else
age=24
if age<18:
    print("No PAN Card")
elif age>60:
    print("You are senior citizen")
else:
    print("hurry,you will get card")

#if two conditions are satisfied it will print first condition
a=300
if a>100:
    print("yes")
elif a>200:
    print("yeah")
elif a>300:
    print("yeahh")
else:
    print("no")
