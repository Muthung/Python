def copyRandomList(head):
    if not head:
        return None
    
    # Step 1: Create a mapping of original nodes to copied nodes
    mapping = {}
    
    # Step 2: Create copied nodes and populate the mapping
    current = head
    while current:
        mapping[current] = Node(current.val)
        current = current.next
    
    # Step 3: Update next and random pointers for copied nodes
    current = head
    while current:
        if current.next:
            mapping[current].next = mapping[current.next]
        if current.random:
            mapping[current].random = mapping[current.random]
        current = current.next
    
    return mapping[head]