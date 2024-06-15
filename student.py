
class A:
    def __init__(self,name=None,usn=None,marks=None,sub=None):
        a=[]
        self.name=name
        self.usn=usn
        self.marks=marks
        self.sub=sub
    def create(self):
        self.name=input("enter the name") 
        self.usn=input("enter the usn")
        self.marks=int(input("enter the marks"))
        self.sub=input("enter the sub")
    def perform(self):
        per = (self.marks*5)/100 
        print(f"Name: {self.name}, USN: {self.usn}, Marks: {self.marks}, Subject: {self.sub}, Performance: {per}%")
        if per>90 and per<90:
            print("good")
        elif per>50 and per<50:
            print("pass")
class students:
    def __init__(self):
        s=[]
    def create(self):
        mani=A()
        mani.create()
        mani.append(students)
    def read(self):
        if self.start is not None:
            print("successfully")
            for i in range(self.start):
            mani.create()
obj =A()
for  _ in range(5):
    obj.create()
    obj.perform()