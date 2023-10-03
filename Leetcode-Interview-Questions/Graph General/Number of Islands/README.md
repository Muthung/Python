## Number of Islands

### Question

Given an *m x n* 2D binary grid *grid* which represents a map of *'I'*s (land) and *'0'*s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all our adges of the grid are all surrounded by water

#### Implemetation

Use Depth-First Approach (DFS) to traverse the grid and count the number of islands.

*numIslands* fucntion uses a nested *dfs* function to perform a depth-first search approach for each "1" encountered in the grid. 

When it encounters a "1", it marks it as '0' (indicating that it's been vivited) and recursively explores its adjacent cells to mark all connected land as visited.

The outer loop iterates through all grid cells and calls the DFS function whenever a '1' is encountered. 

It returns the count of islands found in the grid.
