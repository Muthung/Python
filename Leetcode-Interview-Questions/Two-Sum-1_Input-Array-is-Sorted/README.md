## Two Sum 2 - Input Array is sorted

### Question 

Given a **1-indexed** array of integers *numbers* that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific *target* number. Let those numbers be *numbers[index1]* and *numbers[index2]* where *1 <= index1 < index2 < numbers.length*.

Return the indices of the two numbers, *index1* and *index2*, added by one as an integer array *[index1, index2]* of length 2.

The tests are generated such that there is **exactly  one solution**. You may not use the same element twice.

Your solution must use only constant extra space.

#### Implementation 

Use the two-ponter approach. Since the array is sorted in non-descreasing order, it can maintain two pointers, one pointing to the beginning of the array and the other pointing to the end.

Initialize the left pointer to the first element and the right pointer to the last element.

Compare the sum of the elements at the left and right pointers with the target number.

If the sum is equal to the target, we have found the solution.

If the sum is greater than the target, move the right pointer one step to the left to decrease the sum.

If the sum is less than the target, move the left pointer one step to the right to increase the sum.

Continue the process until a pair of numbers that sum up to the target is found or until the left pointer becomes greater than the right pointer, indicating that no such pair exists.
