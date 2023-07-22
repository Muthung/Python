## Product of Array Except Self 

### Question 

Given an integer array *nums*, return an array *answer* such that *answer[i]* is equal to the product of all the elements of *nums* except *nums[i]*.

The product of any prefix or suffix of *nums* is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

#### Implementation 

Initialize an empty result array of the same length as the input array *nums*.

Iterate over the *nums* array from left to right and calculate the prefix product. Store the product at each index in the result array.

Iterate over the *nums* array from the right to left and calculate the suffix product. Multiply the suffix product with the corresponding value in the result array.

The result array will now contain the product of all elements except the element at each index, fulfilling the requirements of the problem.

The algorithm solves the problem by calculating the product of all elements except the current element efficiently in O(n) time complexity.
