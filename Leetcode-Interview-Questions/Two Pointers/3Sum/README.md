## 3Sum

### Question 

Given an integer array *nums*, return all the triplets *[nums[i], nums[j], nums[k]]* such that *i != j, i != k, and j != k*, and *nums[i] + nums[j] + nums[k] == 0*.

Notice that the solution set must not contain duplicate triplets.

### Implementation 

Use the two-pointer technique.

Sort the nums array in ascending order.

Initialize an empty list called result to store the triplets.

Iterate through the nums array from index 0 to n-3, where n is the length of the array.

If the current element is greater than zero, break out of the loop. (Since the array is sorted, the subsequent elements will also be greater than zero, and their sum will be greater than zero.)

If the current element is the same as the previous element, continue to the next iteration to avoid duplicates.

Initialize two pointers, left and right, where left is the next element after the current element, and right is the last element in the array.

While left is less than right:

    Calculate the sum of the current element, nums[left], and nums[right].
    If the sum is zero, append [nums[i], nums[left], nums[right]] to the result list.
    Move left to the right to avoid duplicates.
    Move right to the left to avoid duplicates.
    If the sum is less than zero, increment left by one.
    If the sum is greater than zero, decrement right by one.
    
Return the result list.
