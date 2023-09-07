## Sum Root to Leaf Numbers

### Question

You are given the *root* of a binary tree containing digits from *0* to *9* only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path *1 -> 2 -> 3* represents the number *123*.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

#### Implementation

The *sumNumbers* function performs a DFS traversal starting from the root. It recursively calculates the sum of each root-to-leaf path by continously updating the *currentSum* variable as it traverses down the tree.

When a leaf node is reached, it returns the current path sum, and these sums are summed up as the DFS recurses back up the tree.

The base case checks if node is None (indicating an empty subtree) and return 0 in that case.

The function returns the total sum of all root-to-leaf numbers.