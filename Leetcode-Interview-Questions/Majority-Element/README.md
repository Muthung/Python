## Majority element

### Question

Given an array *nums* of size *n*, return the majority element.

The majority element is an element that appears more the *[n / 2]* times. You may assume the majority element always exists in the array.

#### Implementation

Boyer-Moore Voting algorithm allows to find the majority element in linear time complexity, which is more efficient than other approaches.

Initialise *storage* - represents the current potential majority element and *steps* - keeps track of its count, variables.

Iterate through each element in the array *nums*.

If *steps* is zero, update *storage* with the current element and set *steps* to 1.
This happens when we haven't found a potential majority element so far or have canceled out all previous elements.

If the current element is the same as *storage*, increment *steps* by 1, indicating another occurence of the potential majority element.

If the current element is different from *storage*, decrement *steps* by 1, as we found an element that cancels out one occurence of the potential majority element.

After iterating through all elements, the *storage* will represent the majority element.
