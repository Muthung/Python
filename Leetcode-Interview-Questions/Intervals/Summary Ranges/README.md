## Summary Ranges

### Question 

You are given a sorted unique integer array *nums*.

A range *[a,b]* is the set of all integers from *a* to *b* (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of *nums* is covered by exactly one of the ranges, and there is no integer *x* such that *x* is in one of the ranges but not in *nums*.

Each range *[a,b]* in the list should be output as:

    *"a->b"* if *a != b*
    *"a"* if *a == b*

### Implementation

Iterate through the sorted array *nums* and construct the ranges based on consecutive numbers. 

Whenever there is a gap between consecutive numbers, create a range from the starting number to the previous number in the sequence. 

If the current number is the last number in the array, create a range from the starting number to the current number.

The function takes the sorted integer array *nums* as input and returns the smallest sorted list of ranges as described in the problem statement. 

The ranges list stores the result, and then adds the ranges in the correct format based on the conditions in the loop. 

Finally, it returns the ranges list as the output.