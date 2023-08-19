class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
def partition(self, head, x):
    bf_head = ListNode()
    bf = bf_head
    af_head = ListNode()
    af = af_head
    
    current = head
    
    while current:
        if current.val < x:
            bf.next = current
            bf = bf.next
        else:
            af.next = current
            af = af.next
            
        current = current.next
    
    af.next = None
    bf.next = af_head.next
    
    return bf_head.next