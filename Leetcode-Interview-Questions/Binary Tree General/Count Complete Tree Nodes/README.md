## Count COmplete Key Nodes

### Question

GIven the *root* of a complete binary tree, return the number of the nodes in the tree.

According to **Wikipedia**, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible.

It can have between *1* and *2* nodes inclusive at the last level *h*.

Design an algorithm that runs in less than *0(n)* time complexity.

#### Implamentation

The *countNodes* function calculates the number of nodes in the complete binary tree.

First, it checks if the root is *None*, and if so, returns 0 (base case for an empty tree).

It then calculates the heights of the left and right subtrees by traversing down the left and right paths of the tree until there are no more left or right children. This effectively counts the levels of the left and right subtrees.

If the left and right heights are equal, the tree is a perfect binary tree, and use bit manipulation (left shift) to calculate the number of nodes (2^(height+1) - 1).

If the heights are not equal, it means the tree is not perfect, so  recursively count nodes in the left and right subtrees and add 1 for the root node.