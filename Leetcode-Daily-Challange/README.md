## Lat Day Where You Can Still Cross

### question

There is a **1-based** binary matrix where *0* represents land and *1* represents water. You are given integers *row* and *col* representing the number of rows and colimns in the matrix, respectively.

Initially on day *0*, the **entire** matrix is **land**. However, each day a new cell becomes flooded with
**water**. You are given a **1-based** 2D array *cells*, where *cells[i] = [ri, ci]* represents that on the 
*ith* day, the cell on the *ri-th* row and *ci-th* column (**1-based** coordinates) will be covered with **water** (i.e., changed to *1*).

You want to find the **last** day that it is possible to walk from **top** to the **bottom** by only walking on land cells. You can start from *any* cell in the top row and end at *any* cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the *last* day where it is possible to walk from the *top* to the *bottom* by only walking on land cells.

#### implementation

Used a binary search algorithm approach, starting with the range of possible days from 0 to the maximum 
number of cells, and iteratively narrow down the range until the last day is found.

Initialize the range of possible days from 0 to the maximum number of cells.

    *left = 0*
    *right = row(col)*

While left is less than or equal to right.

    *set mid as the middle value between left and right:
     mid = left + (right - left)/2*
    *create a new matrix called flooded with dimensions row x col, initialized with all 0s.*
    *for each cell in cells up to day mid, set the corresponding cell in flooded to 1.*
    *if there exists a path from the top row to the bottom row in flooded, 
     update left = mid + 1 *
     - to check for a path, a depth-first search (DFS) or breadth-first search (BFS) algorithm
       starting from any cell in the top row and checking if we can reach any cell in the bottom
       row while only traversing 0 cells.
     - otherwise, update right = mid - 1.

After the binary search, the value of right represents the last day where it is possible to walk from the 
top to the bottom by only walking on land cells. Return right.

The time complexity of this solution is O(log(row*col)*(row*col)), where log(row*col) represents the number 
of iterations in the binary search, and (row*col) is the complexity of the DFS algorithm in the worst case 
when we hve to visit every cell in the matrix.
