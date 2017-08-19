class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def swapEveryKLevelUtil(root, level, k):
     
    # Base Case 
    if (root is None or (root.left is None and root.right is None ) ):
        return
 
    if (level+1)%k == 0:
        root.left, root.right = root.right, root.left
     
    swapEveryKLevelUtil(root.left, level+1, k)
    swapEveryKLevelUtil(root.right, level+1, k)
 
     
def swapEveryKLevel(root, k):
     
    swapEveryKLevelUtil(root, 1, k)
 

def inorder(root):
     
    # Base Case
    if root is None:
        return
    inorder(root.left)
    print (root.data, end = "")
    inorder(root.right)
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(8)
root.right.left = Node(7)
 
k = 2
inorder(root)
 
swapEveryKLevel(root, k)
inorder(root), k)
inorder(root)