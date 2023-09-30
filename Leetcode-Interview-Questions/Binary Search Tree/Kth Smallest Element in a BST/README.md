## Kth Smallest Element in a BST

### Question

Given the *root* of a binary seacrh tree, and an integer *k*, return the *kth* smallest value (1-indexed) of all the values of the nodes in the tree.

#### Implementation

This follows in-order traversal approach.

It utilizes a stck data structure to efficiently traverse the tree while maintaining the ascending order of elements. 

Starting from the root node, it pushes nodes onto the stack while moving to the left-most node. When it reaches the leftmost leaf node, it pops elements from the stack, decrementing k with each pop operation.

When k reaches 0, it returns the value of the last popped node, which represents the kth smallest element.

This algorithm ensures that it traverses the tree in a sorted order, and it is designed for efficiency, making it suitable for large binary seacrh trees.