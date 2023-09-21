## Binary Tree Level Order Traversal

### Question

Given the *root* of a binary tree, return the level order traversal of it's nodes' values. (i.e., from left to right, level by level).

#### Implementation

The *levelOrder* function takes the root of the binary tree as input and returns the level order traversal of its nodes' values. It initializes an empty list called *result* to store the traversal results and a queue called *queue* to perform a breadth-first approach (BFS).

Inside the main loop, the algorithm processes one level of nodes at a time. It uses a *for* loop with the variable *level_size* to keep track of the number of nodes in the current level. It also initializes an empty list called *level_vals* to store the values of nodes at the current level.

Within the inner loop, the algorithm qequeues nodes from the front of the *queue*, adds their values to the *level_vals* list, and enqueues their left and right children if they exist.

After processing all nodes in the current level, the *level_vals* list contains the values of nodes in that level, which are appended to the *result* list.

The BFS continues until the *queue* is empty, meaning all levels of the binary tree have been processed.

The function returns the *result* list containing the level order traversal of the binar tree.