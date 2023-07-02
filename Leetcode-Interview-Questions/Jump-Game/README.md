## Jump game

### Question 

You are given an integer array *nums*. Youare initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return *true* if you can reach the last index, or *false* otherwise.

#### Implementation 

It can be solved using a Greedy Algorithm approach. 

Iterate through the array and keep track of the fartheest position it can reach from each index.

If at any point, the current index is greater than the farthest position it can reach, that means it cannot reach the last index.

Otherwise, update the farthest position using the current index and the value at that index.

