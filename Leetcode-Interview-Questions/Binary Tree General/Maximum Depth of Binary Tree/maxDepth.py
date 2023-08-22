class TreeNode:
    def  __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def maxDepth(root):
    if root is None:
        return 0
    
    left_d = maxDepth(root.left)
    right_d = maxDepth(root.right)
    
    return max(left_d, right_d) + 1