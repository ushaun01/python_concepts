class Employee:
    def __init__(self,id,sal,name):
        self.id=id
        self.sal=sal
        self.name=name
    def display1(self):
        print(self.id,self.sal,self.name)