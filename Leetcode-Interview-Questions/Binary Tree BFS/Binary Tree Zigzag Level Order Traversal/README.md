## Binary Tree Zigzag Level Order Traversal

### Question

Given the *root* of a binary tree, return the zigzag level order traversal of its nodes values. (i.e., from left to right, then right to left for the next level and alternate between).


#### Implementation

It uses a breadth-first search (BFS) approach. It maintains a queue to keep track of nodes at each level while toggling between left-to-right and right-to-left order for alternate levels. The algorithm starts by initializing an empty result list and a queue containing the root node.

It then enters a loop where it processes each level of the tree. Withing the loop, it iterates through all nodes at the current level, dequeuing them from the queue.

Depending on whwther the level should be traversed in reverse (right-to-left) or not, it either appends the node's value to the level list (for left-to-right) or inserts it at the beginning of the level list (for right-to-left).

After processing all nodes at the current level, it appends the level list to the result.

For each node, if it has left and/or right children, those children are enqueued into the queue for processing in the next level. The algorithm continues this process until all levels have been traaversed, and it returns the resulting list of level-order traveral with zigzag ordering.