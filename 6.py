class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
    def insert(self,value):
        
    def print(self,head):
        if head is None:
            print("list is empty")
            return None
        else:
            temp=self.head
            while temp is not None:
                print(temp.value)
            temp=temp.next
Head=tail=Node(10)
tail.next=Node(20)
tail=tail.next
tail.next=Node(30)
tail=tail.next
tail.next=Node(40)
tail=tail.next
print(Head.value)
print(Head.value)
Head.print()