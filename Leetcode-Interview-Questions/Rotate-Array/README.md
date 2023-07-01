## Rotate array

## Question

Given an integer array *nums*, rotate the array to the right by *k* steps, where *k* is non-negative.

#### Implementation

Method for rotating an array is, to reverse the entire array, then reverse the first *k* elements,  and finally reverse the remaining elements. This approach has a time complexity of 0(n), where *n* is the size of the array.

The best option is to use slicing.

Calculate the effective number of rotations by taking *k* modulo *len(num)*. This ensures that *k* is within valid range of array indices.

Use of slicing to rotate the array. The expression *nums[-k:]* represents the last *k* elements of the array, and *nums[:-k]* represents the remaining elements from the beginning of the array up to the *(len(nums) - k)th* element. By concactenating these two slices, the rotated array is obtained.
