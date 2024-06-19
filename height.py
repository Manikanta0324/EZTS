class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def Height(root):
    if root is None:
        return 0
    lh=Height(root.left)
    rh=Height(root.right)
    return max(lh,rh)+1
def leave(root):
    if root is None:
        return 0
    lh=leave(root.left)
    rh=leave(root.right)
    if lh==0 and rh==0:
        print(root.value)
if __name__ == "__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.right.right.right=Node(10)
    leave(root)
    print("height of the tree=",Height(root))
    