## Surrounded Regions

### Question

Given an *m x n* matrix *board* containing *'X'* and *'0'*, capture all regions that are 4-directionally surrounded by *'X'*.

A region is captured by flipping all *'0'*s into *'X'*s in that surrounded region.

#### Implementation

It uses a Depth First Search (DFS) approach to identify and mark 'O' regions that are not surrounded by 'X'.

The algorithm first takes marks 'O's on the matrix's border as visited and then recursively explores adjacent 'O' cells to mark them as visited as well.

After the DFS traversal, it flips 'O's marked as visited to 'X' while restoring previously marked 'V' cells back to 'O'.

