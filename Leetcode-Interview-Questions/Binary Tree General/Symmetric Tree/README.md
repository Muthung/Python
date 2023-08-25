## Symmetric Tree

### Question

Given the *root* of a binary tree, check whether itis a mirror of itself(i.e., symmetric around its center).

#### Implementation

The function take the root of the binary tree as its argument.

A helper function *isMirror* takes two nodes as arguments: one from the left subtree and one from the right subtree. This function checks whether the two nodes are mirror images of each other.

Inside the *isMirror* function:

- if both nodes are *None*, return *True*, as they are symmetric.

- If only one of the nodes is *None*, return *False*, as they are ot symmetric.

- Check if the values of the two nodes are equal and if the left node's left child is a mirror of the right node's right child, and if the left node's right child is a mirror of the right node's left child.

In the main *isSymmetric* function:

- Check if the root is *None*, and if it is, return *True*.

- Call the *isMirror* function with the left and right subtrees of the root nodes.

