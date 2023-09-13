## Binary Tree Maximum Path Sum.

### Question

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once.

Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the *root* of a binary tree, return the maximum path sum of any non-empty path.

#### Implementation

Within the *max_gain* function, recursively calculate the maximum gain for each subtree. The maximum gain for a subtree is the maximum path sum that starts from that subtree's root node and goes down the tree.

It calculatesthe left and right gains for the current node, ensuring tht negative values are replaced with 0.

It computes the maximum path sum through the current node, which includes the current node's value, the left gain, and the right gain.

Update the global *max_sum* if it finds a higher path sum through the current node.

Call the *max_gain* with the root of the binary tree to find the maximum path sum and return it as the result.
