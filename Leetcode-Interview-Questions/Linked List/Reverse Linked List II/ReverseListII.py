def reverseBetween(head, left, right):
    if not head or left == right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Traverse to the node before the left position
    for _ in range(left - 1):
        prev = prev.next
    
    # Initialize pointers for reversing the sublist
    current = prev.next
    tail = current
    
    prev_reverse = None
    for _ in range(right - left + 1):
        next_node = current.next
        current.next = prev_reverse
        prev_reverse = current
        current = next_node
    
    # Connect the reversed sublist back to the main list
    prev.next = prev_reverse
    tail.next = current
    
    return dummy.next