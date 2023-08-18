class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_right(head, k):
    if not head or k == 0:
        return head
    
    # Calculate the length of the linked list
    length = 1
    current = head
    while current.next:
        length += 1
        current = current.next
    
    # Adjust k to avoid unnecessary rotations
    k = k % length
    
    if k == 0:
        return head
    
    # Find the new head and tail of the rotated list
    current = head
    for _ in range(length - k - 1):
        current = current.next
    
    new_head = current.next
    current.next = None
    
    # Update the tail to point to the original head
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head
    
    return new_head