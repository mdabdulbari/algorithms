from collections import deque
def que(root, v, que_v):
    pointer = root
    if (pointer == None):
        return deque()
    if (pointer.data == v):
        return que_v
    que_v.append(pointer.data)
    que(pointer.left, v, que_v)
    que(pointer.right, v, que_v)  
    return que_v    
    
def lca(root , v1 , v2):
    pointer = root
    que_v1 = deque()
    que_v1 = que(pointer, v1, que_v1)
    
    que_v2 = deque()
    que_v2 = que(pointer, v2, que_v2)
    print(que_v1)
    print(que_v2)