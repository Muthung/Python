## Binary Tree Right Side View

### Question

Given the *root* of a binary tree, imagine yourself standing on the *right side* of it, return the values of the nodes you can see ordered from top to bottom.

#### Implementation

The *rightSideView* function, which take the root of the binary tree as input. Checks if the input tree is empty. If it's empty, return an empty list.

Initialize an empty list *result* to store the visible nodes from the right side and a queue to perform BFS. Start the BFS traversal by adding the root node to the queue.

While the queue is not empty, process each level of the tree. For each level, iterate through the nodes and keep track of the rightmost node at the level. Add the value of the rightmost node to the *result* list.

Enqueue the left and right children of each node if the yexist, ensuring that you process the tree level by level. Return the *result* lsit, which contains the values of the nodes visible from the right side of the binary tree.