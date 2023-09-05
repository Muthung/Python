class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def flatten(self, root):
        if not root:
            return None
        
        right_subtree = root.right
        
        self.flatten(root.left)
        
        root.right = root.left
        root.left = None
        
        current = root
        while current.right:
            current = current.right
        
        current.right= right_subtree
        
        self.flatten(right_subtree)
        