## Construct Binary Tree from Inorder and Postorder Traversal.

### Question

Given two integer arrays *inorder* and *postorder* where *inorder* is the inorder traversal of a binary tree and *postorder* is the postorder traversal of the same tree, construct and return the binary tree.

#### Implementation

The *buildTree* function takes the inorder and postorder lists as input and constructs the binary tree recursively.

It first pops the last element from the post order list to get the root value, then finds the index of the root value in the inorder list.

Based on this index, it separates the inorder and postorder lists for the left and right subtrees and recursively builds the left and right subtrees.

It returnns the root of the constructed binary tree.

The *printTree* function performs an inorder traversal of the tree to print the values of the nodes in the constructed binary tree.
