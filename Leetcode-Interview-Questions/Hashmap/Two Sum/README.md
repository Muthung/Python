## Two Sum

### Question 

Given an array of integers *nums* and an integer *target*, return indices of the two numbers such that they add up to *target*.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

#### Implementation

In the function, initialize an empty dictionary *num_toIndex* to store the numbers and their indices.

Iterate through the *nums* array using a for loop. For each number, calculate its complement (the number needed to reach the target) by subtracting it from the target.

If the complement is already present in the *num_toIndex* dictionary, it means, found the pair that adds up to the target. Return the indices of the current number and its complement from the dictionary.

If the complement is not in the dictionary, store the current number and its index in the dictionary for future reference.
    
If there is no solution (no pair adds up to the target), the function will return an empty list.

This solution has a time complexity of O(n) because it iterates through the *nums* array only once, and a space complexity of O(n) to store the numbers and their indices in the dictionary.
