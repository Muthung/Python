def getMinimunDifference(self, root):
    def inorder(node):
        if not node:
            return []
        
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    values = inorder(root)
    min_diff = float('inf')
    
    for i in range(1, len(values)):
        min_diff = min(min_diff, values[i] - values[i - 1])
        
    return min_diff