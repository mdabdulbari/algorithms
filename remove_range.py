def remove_range(head, start, end):
    assert(start <= end)
    # Case: remove node at head
    if start == 0:
        for i in range(0, end+1):
            if head != None:
                head = head.next
    else:
        current = head
        # Move pointer to start position
        for i in range(0,start-1):
            current = current.next
        # Remove data until the end
        for i in range(0, end-start + 1):
            if current != None and current.next != None:
                current.next = current.next.next
    return head