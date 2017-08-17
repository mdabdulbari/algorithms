class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
class LinkedList:

    def __init__(self, list):
        self.head = Node(0)
        previous = self.head
        for i in range(len(list) - 1):
            node = Node(i + 1)
            previous.next_node = node
            previous = node

list = [e for e in range(10)]
linked_l = LinkedList(list)

n = 5
count = -1
pointer = Node(100)
pointer.next_node = linked_l.head
pointer2 = Node(200)
pointer2.next_node = linked_l.head
while(pointer2 != None):
    count += 1
    pointer2 = pointer2.next_node
    if (count > n):
        pointer = pointer.next_node

print(pointer.value)