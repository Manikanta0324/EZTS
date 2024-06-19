#class stack:
    def __init__(self,item=None):
        self.item=[]
    def valid(self,x):
        if self.x=='[' or self.x=='{' or self.x=='(':
            self.item.append(x)
        elif self.x==')' or self.x=='}' or self.x==')':
            self.item.pop(x)
e="[3+7{52/11}(3+5)]"
s=stack()
ob="[{("
cb=")}]"
flag=0
for i in e:
    if i in ob:
        s.push(i)
    if i in cb:
       x= s.pop()
    if x=="(" and i==")":
        pass
    elif x=="{" and i=="}":
        pass
    elif x=="[" and i=="]":
        pass
    else:
        flag==1
        break
if flag==0:
    print("valid")
else:
    print("invalid")#



