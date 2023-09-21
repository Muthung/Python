def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_vals = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.pop(0)
            level_vals.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level_vals)
    
    return result