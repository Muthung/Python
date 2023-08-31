## Populating Next Right Pointers in Each Node II.

### Question

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to *NULL*.

Initially, all next pointers are set to *NULL*.

#### Implementation

The *connect* function takes the root of the binary tree as input and populates the *next* pointers for each node. The function uses a level-order traversal approach with constant extra space.

The *level_size* pointer is used to keep track of the leftmost node in each level. The outer loop iterates over the levels, and the inner loop iterates over nodes within the same level, connecting their children and adjusting the *next* pointers accordingly.