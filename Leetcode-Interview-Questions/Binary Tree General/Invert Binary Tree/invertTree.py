class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def invertTree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left
    
    ## Add a self.invertTree to avoid undefined error during compiling.
    
    invertTree(root.left)
    invertTree(root.right)
    
    return root