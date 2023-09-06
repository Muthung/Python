## Path Sum

### Question

Given the *root* of a binary tree and an integer *targetSum*, return *true* if the tree haas a **root-to-leaf** path such that adding up all the values along the path equals *targetSum*.

A *leaf* is a node with no children.

#### Implementation

The *hasPathSum* function is a recursive DFS function that checks if there's a path from thr root to a leaf node with the given target sum.

It returns *True* if such a path exists, and *False* otherwise. The function handles edge cases such as an empty tree.