def rightSideView(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        
        levelLength = len(queue)
        for i in range(levelLength):
            node = queue.pop(0)
            
            if i == levelLength - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
    
    return result