## Average of Levels in Binary Tree

### Question

Given the *root* of a binary tree, return the average value of the nodes on each level in the form of an array.

Answers within *10^-5* of he actual answer will be accepted.

#### Implementation

This uses a level-order traversal (BFS) approach to compute the average values of nodes on each level of the binary tree. It starts by initializing an empty list called *result* to store the average values.

A queue is used to perform the BFS. It begins by adding the root node to the queue.

Inside the main loop, It process nodes at each level. It keeps track of the sum of nodes values (*level_sum*) and the count of nodes at the current level (*level_count*). It iterate through all nodes in the current level, adding their values to *level_sum*.

Each node, if it has left and/or right children, it enqueue those children to the queue for procesing in the next level.

After processing all nodes in the current level, it calculates the average value fo rthat level by diving *level_sum* by *level_count*, converting it to a floating-point number, and append it to the *result* list.

This process continues until all levels of the tree have been traversed. Finally, the *result* list conatins the average values of nodes at each level, and it is returned as the output.s