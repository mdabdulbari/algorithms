def is_sorted(head):
    if not head:
        return True
    current = head
    while current.next:
        if current.val > current.next.val:
            return False
        current = current.next
    return True