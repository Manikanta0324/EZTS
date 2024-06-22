class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        self.height=1
def insert(root,super):
    if not root:
        return node(super)
    if super<root.value:
        root.left=insert(root.left,super)
    else:
        root.right=insert(root.right,super)
    root.height=1+max(ght(root.left),ght(root.right))
    bf=getbf(root)
    #rr rotation
    if bf>1 and super<root.left.value:
        return rightRotate(root)
    #rl rotation
    if bf>1 and super>root.left.value:
        root.left=leftRotate(root.left)
        return rightRotate(root)
    #ll rotation
    if bf<-1 and super<root.right.value:
        return leftRotate(root)
    #lr
    if bf<-1 and super<root.right.value:
        root.right=rightRotate(root.right)
        return leftRotate(root)
    return root
def ght(root):
    if not root:
        return 0
    return root.height
def getbf(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)
def leftRotate(A):
    b=A.right
    temp=b.left
    b.left=A
    A.right=temp
    A.height=1+max(ght(A.left),ght(A.right))
    b.height=1+max(ght(b.left),ght(b.right))
    return b
def rightRotate(A):
    b=A.left
    temp=b.right
    b.right=A
    A.left=temp
    A.height=1+max(ght(A.left),ght(A.right))
    b.height=1+max(ght(b.left),ght(b.right))
    return b
def inorder(root):# print the data inorder format
    if not root:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
if __name__=='__main__':
    root=None
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in vl:
        root=insert(root,i) 
    inorder(root)      
