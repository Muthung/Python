## Flatten Binary Tree to Linked List.

### Question

Given the *root* of a binary tree, flatten the tree into a "linked list":

- The linked list should use the sa,e *TreeNode* class where the *right* child pointer points to the next node in the list and the *left* child pointer is always *null*.

- The lined list should be in the same order as a **pre-order traversal** of the binsary tree.

#### Implementation

The *flatten* function, recursively flatten the left subtree, make the left subtree the new right subtree of the current node.

Traverse to the end of the new right subtreee, attach the oroginal right subtree to the end of the new right subtree.

Recursively flatten the original right subtree, repreat this process for each node in the tree.