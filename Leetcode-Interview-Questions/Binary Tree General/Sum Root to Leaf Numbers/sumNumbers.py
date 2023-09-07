def sumNumbers(root):
    def dfs(node, currentSum):
        if not node:
            return 0
        
        currentSum = currentSum * 10 + node.val
        
        if not node.left and not node.right:
            return currentSum
        
        leftSum = dfs(node.left, currentSum)
        rightSum = dfs(node.right, currentSum)
        
        return leftSum + rightSum
    
    return dfs(root, 0)