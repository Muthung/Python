def zigzagLevelOrder(root):
    if not root:
        return []
    
    result = []
    queue = collections.deque([root])
    reverse = False
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            if reverse:
                level.insert(0, node.val)
            else:
                level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        result.append(level)
        reverse = not reverse
    
    return result