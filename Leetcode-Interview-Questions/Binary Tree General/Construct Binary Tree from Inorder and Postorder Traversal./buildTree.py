class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    
    root_val = postorder.pop()
    root = TreeNode(root_val)
    inorder_index = inorder.index(root_val)
    
    root.right = buildTree(inorder[inorder_index + 1:], postorder)
    root.left = buildTree(inorder[:inorder_index], postorder)
    
    return root

def printTree(root):
    if root is not None:
        printTree(root.left)
        print (root.val)
        printTree(root.right)