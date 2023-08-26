## Construct Binary Tree from Preorder and Inorder Traversal

### Question

Given two integer arrays *preorder* and *inorder* where *preorder* is the preorder traversal of a binary tree and *inorder* is the inorder travrsal of the same tree, construct and return the binary tree.

#### Implementation

The function constructs the binary tree based on the *preorder* and *inorder* traversals. It returns the root of the constructed tree. 

The pop function is used to retrieve the *root* element from the preorder list while also removing it from the list.