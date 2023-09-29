## Minimum Absolute Difference in BST.

### Question

Given the *root* of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

#### Implementation

There is a *TreeNode* to represent nodes in BST and a *Solution* class with the *getMinimumDifference* method to calculate the minimum absolute difference. 

It uses in-order traversal to collect values in sorted order and then calculates the minimum difference between adjacent values.

