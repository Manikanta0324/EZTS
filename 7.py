class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linked:
    head=None
    tail=None
    length=0
    def front(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    def dfront(self):
        if self.head is None:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.length=-1
    
    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

obj=Linked()
obj.front(100)
obj.front(200)
obj.front(300)
obj.dfront()
obj.print()