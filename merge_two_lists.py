class Node:

    def __init__(self, x):
        self.val = x
        self.next = None

def merge_two_list(l1, l2):
    ret = cur = Node(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return ret.next

# recursively
def merge_two_list_recur(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = merge_two_list_recur(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_list_recur(l1, l2.next)
        return l2