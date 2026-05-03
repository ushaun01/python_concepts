#1: calling a function multiple times
def login():
    username="usha"
    password=1234
    print(username)
    print(password)
login()
login()
login()

#2: passing parameters
def log(a,b):
    name=a
    age=b
    print("My name is",name)
    print("My age is",age)
log("usha",25)
log("pranita",30)

#3:
def log(a):
    name=a
    age=30
    print("My name is",name)
    print("My age is",age)
log("usha")
log("pranita")

#4:
def log(a,b=25):
    name=a
    age=b
    print("My name is",name)
    print("My age is",age)
log("usha")
log("pranita",30)
