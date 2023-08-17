class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
def deleteDuplicates(head):
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next
    
    return dummy.next