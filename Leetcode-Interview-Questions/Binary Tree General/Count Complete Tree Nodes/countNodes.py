def countNodes(root):
    if not root:
        return 0
    
    # Calculate the height of the left subtree
    left_height = 0
    node = root
    while node.left:
        left_height += 1
        node = node.left
    
    # Calculate the height of the right subtree
    right_height = 0
    node = root
    while node.right:
        right_height += 1
        node = node.right
    
    # If left and right heights are equal, the tree is a perfect binary tree
    if left_height == right_height:
        return (1 << (left_height + 1)) - 1  # Calculate the number of nodes using bit manipulation
    else:
        # Recursively count nodes in the left and right subtrees
        return 1 + countNodes(root.left) + countNodes(root.right)