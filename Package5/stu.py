class Student:
    def __init__(self,sid,grade,names):
        self.sid=sid
        self.grade=grade
        self.names=names
    def displaystu(self):
        print(self.sid,self.grade,self.names)