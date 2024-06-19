class Stack:
    def __init__(self):
        self.item=[]
    def push(self,data):
        self.item.append(data)
    def pop(self):
         return self.item.pop()
    def size(self):
        return len(self.item)
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
print(s.item)
print(s.size())
