def connect(root):
    if not root:
        return root
    
    queue = [root]
    
    while queue:
        level_size = len(queue)
        prev_node = None
        
        for i in range(level_size):
            curr_node = queue.pop(0)
            
            if prev_node:
                prev_node.next = curr_node
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            
            prev_node = curr_node
            
    return root