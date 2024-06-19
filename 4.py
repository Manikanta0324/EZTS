#queue
class queue:
    def __init__(self):
        self.item=[]
    def push(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
    
m=queue()
m.push(10)
m.push(20)
m.push(30)
m.pop()
print(m.item)
print(m.pop())
print(m.item)