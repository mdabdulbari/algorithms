class Node():
    def __init__(self, val=None):
        self.val = int(val)
        self.next = None


def print_linked_list(head):
    string = ""
    while head.next:
        string += str(head.val) + " -> "
        head = head.next
    string += str(head.val)
    print(string)


def partition(head, x):
    left = None
    right = None
    prev = None
    current = head
    while current:
        if int(current.val) >= x:
            if not right:
                right = current
        else:
            if not left:
                left = current
            else:
                prev.next = current.next
                left.next = current
                left = current
                left.next = right
        if prev and prev.next is None:
            break
        # cache previous value in case it needs to be pointed elsewhere
        prev = current
        current = current.next


def test():
    a = Node("3")
    b = Node("5")
    c = Node("8")
    d = Node("5")
    e = Node("10")
    f = Node("2")
    g = Node("1")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    print_linked_list(a)
    partition(a, 5)
    print_linked_list(a)


if __name__ == '__main__':
    test()