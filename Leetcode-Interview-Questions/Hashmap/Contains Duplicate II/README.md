## Contains Duplicate II

### Question 

Given an integer array *nums* and an integer *k*, return *true* if there are two **distinct indices** *i* and *j* in the array such that *nums[i] == nums[j]* amd *abs(i - j) <= k*.

#### Implementation 

Use a hash map to keep track of the elements you have seen so far and their corresponding indices.

As you traverse the array, you can check if the current element already exists in the hash map. If it does, you check if the absolute difference between the current index and the previously seen index is less than or equal to *k*. 

If it is, then you have found two distinct indices with the same value within the given range, and you can return true. If not, you continue traversing the array.

The function takes an array *nums* and an integer *k* as input and returns *True* if there are two distinct indices with the same value within the range *k*, otherwise, it returns *False*.