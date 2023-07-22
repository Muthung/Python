## Game of Life 

### Question 

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an *m x n* grid of cells, where each cell has an initial state: live (represented by a *1*) or dead (represented by a *0*). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the *m x n* grid *board*, return the next state.

#### Implementation 

Create a helper function to count the live neighbors of a cell. This function will check the eight neighboring cells of the given cell and count the number of live cells around it.

Iterate through each cell of the board and apply the rules of the Game of Life to calculate the next state for each cell. You can do this by creating a new grid to store the next state and updating each cell based on its current state and the number of live neighbors.
