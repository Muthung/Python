## Validate Binary Search Tree

### Question

Given the *root* of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left **subtree** of a node contains only nodes with keys less than the node's key.

- The right subtree of a node contains only nodes with keys greater than the node's key.

- Both the left and right subtrees must also be binary search trees.

#### Implementation

Use a recursive approach.

Start with the root node of the tree. At each node, it check if it satisfies the conditions of being a BST, which means its value should be within a certain range. Initially, the range is considered as negative infinity to positive infinity. As it traverse the tree,it updates the range accordingly.

For each node, it checks if its value is within the current range (between the minimum and maximum values allowed). If it is, it recursively check its left and right subtrees, passing the updated range as it move down the tree. If both the left and right subtrees satisfy the BST conditions, then the entire tree is a valid BST.

If any node violates the BST conditions by having a value outside the current range, you return False immediately, indicating that the tree is not a valid BST.