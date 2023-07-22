## Jump Game 2

### Question 

You are given a **o-indexed** array of integers *nums* of length *n*. You are initially positioned at *nums[0]*.

Each element *nums[i]* represents a maximum length of a forward jump from index *i*. In other words, if you ae at *nums[i]*, you can jump at any *nums[i + j]* where:

>    *0 <= j <= nums[i]* and
>    *i + j < n*

Return the minimum number of jumps to reach *nums[n - 1*. The test cases are generated such that you can reach *nums[n - 1*.

#### implementation 

This is solved using Dynamic Programming approach.

Define an array called *jumpGame* of length *n*, where *jumpGame* represents the minimum number of jumps needed to reach index *i*.

Initialize all elements of *jumpGame* with a maximum value except for *jumpGame[0]*, which is 0 since it  start at index 0. Then, for each index *i* from *1* to *n - 1*, we can update *jumpGame[i]* by considering all possible jumps from previous indices.

Initialize *jumpGame* array with a maximum value.

Set *jumpGame[0]* since it starts at index *0**.

Iterate through the array from index *1* to *n - 1*.

> For each index *i*, iterate from index 0 to i - 1.
>> Check if it can reach index *i* from index *j (0 <= j < i*.
>> If it cn reach index *i* from index *j*, update *jumpGame[i]* as the minimum of its current value and 
>> *jumpGame[j] + 1*.

Return *jumpGame[n - 1*, which represents the minimum number of jumps needed to reach the last index.

