## Maximum Depth of Binary Tree

### Question

Given the *root* of a binary tree, retur its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the roof node down to the farthest leaf node.

#### Implementation

**maxDepth** Function: The main function *maxDepth* takes a single argument, which is the root node of the binary tree. It calculates the maximum depth of the tree.

**Base Case**: If the *root* node is *None*, it means we've reached the end of the tree or a leaf node. In this case, the depth is 0.

**Recursive Approach**: If the *root* node is not *None*, we calculate the maximum depth of its left subtree using a recursive call to *maxDepth(root.left)*. Similarly, we calculate the maximum depth of its right subtree using *maxDepth(root.right)*.

**Returning the Maximum Depth**: We then compare the depths of the left and right subtrees and take the maximum of the two. To get the maximum depth of the entire tree, we add 1 to the maximum of the left and right depths.