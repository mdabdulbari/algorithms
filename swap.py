class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree():
    root = Node(1)
    n = int(input())
    pointer = root
    for i in range(n):
        list1 = list(map(int, input().split()))
        pointer.left, pointer.right = list1[0], list1[1]
        
def buildTree():
    root = Node(1)
    n = int(input())
    nodes = []
    nodes.append(root)
    for i in range(n):
        list2 = list(map(int, input().split()))
        a, b = Node(list2[0]), Node(list2[1])
        nodes.append(a)
        nodes.append(b)
    root.left = nodes[1]
    root.right = nodes[2]
    
    i = 1
    j = 3
    while(i != len(nodes) -4):
        nodes[i].left = nodes[j]
        nodes[i].right = nodes[j + 1]
        i += 1
        j += 2
    return root, nodes
    
def printTree(root):
    if root == None:
        return
    printTree(root.left)
    if(root.data != -1):       
        print(root.data, end = " ")
    printTree(root.right)

def nodes_at_level(nodes, level):
    a = (2 ** (level - 1) )- 1
    b = a + 2 ** (level - 1)
    return nodes[a:b]

def swap(nodes):
    for e in nodes:
        e.left, e.right = e.right, e.left

root, nodes = buildTree()    
k = int(input())
h1 = int(input())
h2 = int(input())
swap(nodes_at_level(nodes, 1))
printTree(root)