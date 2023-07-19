## Spiral Matrix 


### Question 

Given an *m x n**matrix*, return allelements of the *matrix* is spiral order.

#### Implementation 

To achieve this, use a simple algorithm that moves along the border of the matrix while collecting the elements inthe desired order.

The *spiral_order* function iterates through the matrix in a spiral manner, extracting the elements from each side(top, right, bottom, left) one by one.

The result list will contain all the elements of the matrix in the desired spiral order.
