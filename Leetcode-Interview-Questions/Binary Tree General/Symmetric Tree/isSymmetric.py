class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def isMirror(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    if root is None:
        return True
    