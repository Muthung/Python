## Minimum Size Subarray Sum 

### Question 

Given an array of positive integers *nums* and a positive integer *target*, return the minimal length of a
subarray whose sum is greater than or equal to *target*. If there is no such subarray, return *0* instead.

### Implementation 

Use the sliding window technique.

Maintain two pointers, left and right, to represent the current subarray under consideration.

Keep moving the right pointer to expand the subarray until the sum of the subarray is greater than or equal to the target. 

Then update the minimal length of the subarray, and move the left pointer to contract the subarray and find a shorter subarray that satisfies the condition.

Repeat this process until we reach the end of the array.
