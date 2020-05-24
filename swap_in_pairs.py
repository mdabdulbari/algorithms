class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swap_pairs(head):
    if not head:
        return head
    start = Node(0)
    start.next = head
    current = start
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        current.next = second
        current.next.next = first
        current = current.next.next
    return start.next