class TreeNode:
    def __init__(self, val = 0, left = 0, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        
        root.left = self.buildTree(preorder, inorde[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1:])
        
        return root