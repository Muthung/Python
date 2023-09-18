## Lowest Common Ancestor of a Binary Tree

### Question

Given a binary tree, find the lowest common ancestor (LCA) of two given nides in the tree.

According to the **definition of LCA on Wikipedia**: " The lowest common ancestor is defined between two nodes *p* and *q* as the lowest node in *T* that has both *p* and *q* as descendants ( where we allow **a node to be a descendant of itself** ).

### Implemenatation

The *lowestCommonAncestor* function takes the root of the tree and two nodes *p* and *q* as input.

It starts by checking if the current node is either *p* or *q*. If it is , it returns it as a potential common ancestor.

It then recursively search for *p* and *q* in the left and right subtrees of the current node.

If both *left* and *right* are not *None*, it means *p* and *q* are found in different subtrees, so the current node is the LCA.

If either *left* or *right* is *None*, it means both *p* and *q* are in the same subtrees, so it returns the non-None result.
