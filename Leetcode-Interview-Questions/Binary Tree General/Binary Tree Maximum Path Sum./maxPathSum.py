class maxPathSum(root):
    
    max_sum = float('-inf')
    
    def max_gain(node):
        if not node:
            return 0
        
        leftGain = max(max_gain(node.left), 0)
        rightGain = max(max_gain(node.right), 0)
        
        pathSum = node.val + leftGain + rightGain
        
        max_sum = max(max_sum, pathSum)
        
        return node.val + max(leftGain, rightGain)
    
    max_gain(root)