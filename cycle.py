#inclue<python.h>

class Node:

    def __init__(self, value, next_node = None):

        self.value = value
        self.next_node = next_node
    
    def getValue(self):

        return self.value

    def getNext_node(self):

        return self.next_node

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, value):

        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
            return
        pointer = self.head
        while(pointer.next_node != None):
            pointer = pointer.next_node
        pointer.next_node = new_node
    
    def __len__(self):

        count = 0
        for i in self:
            count += 1
        return count

    def __str__(self):
        
        string = ""
        for i in self:
            string = string + str(i) + ","
        return string

    def __iter__(self):

        pointer = self.head
        while(pointer != None):
            yield pointer.value
            pointer = pointer.next_node

    def cycle(self):
        
        pointer = self.head
        while(pointer != None and pointer.next_node != None):
            pointer = pointer.next_node
        pointer.next_node = self.head.next_node.next_node.next_node
    
    def has_cycle(self):

        if (self.head == None and self.head.next_node == None):
            return False
        pointer1 = self.head
        pointer2 = self.head.next_node
        
        while(pointer2 != None):
            if (pointer1 == pointer2):
                return True
            pointer1 = pointer1.next_node
            if (pointer2.next_node == None):
                return False
            pointer2 = pointer2.next_node.next_node
        return False


l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
l.push(6)
l.push(7)
l.push(8)
l.push(9)
l.push(10)
l.push(11)
l.push(12)
l.push(13)
l.push(14)
l.cycle()
print(l.has_cycle())            