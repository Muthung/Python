## Invert Binary Tree

### Question

Given the *root* of a binary tree, invert the tree, and return its root.

#### Implementation

Define the *invertTree* function that takes the root of the binary tree as its argument.

Check if the current node is *None*, which means it's a leaf node. If it's a leaf node, return *None*.

Swap the left and right children of the current node using a simoultenous assignment. This effectively inverts the structure of the subtree rooted at the current node.

Recursively call *invertTree* on the left and right children of the current node. Thi will invert the entire left and right subtrees.

Return the root node of the inverted tree.

