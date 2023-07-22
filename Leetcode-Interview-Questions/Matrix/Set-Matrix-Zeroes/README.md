## Set Matrix Zeroes

### Questions 

Given an *m x n* integer *matrix*, if an element is *0*, set t=its entire row and column to *0s*.

You must do it in place.

#### Implementation 

Create two sets to keep track of the rows and columns that need to be zeroed out.

Traverse through the matrix, and whenever you encounter a *0*, add its row index and column index to the respective sets.

After the first pass, iterate through the sets and zero out the rows and columns in the matrix accordingly.
