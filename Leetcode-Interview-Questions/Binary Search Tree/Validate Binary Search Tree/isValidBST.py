def is_valid_BST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    if not min_val < root.val < max_val:
        return False
    
    return (is_valid_BST(root.left, min_val, root.val) and
            is_valid_BST(root.right, root.val, max_val))