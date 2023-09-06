class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        def dfs(node, currentSum):
            if not node.left and not node.right and currentSum + node.val == targetSum:
                return True
            
            left_result = dfs(node.left, currentSum + node.val) if node.left else False
            right_result = dfs(node.right, currentSum + node.val) if node.right else False
            
            return left_result or right_result
        
        return dfs(root, 0)