## Longest Consecutive Sequence 

### Question 

Given an unsorted array of integers *nums*, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in *O(n)* time.

#### Implementation

Create a set to store all the elements in the input array.

Initialize a variable *longest_streak* to 0, which will keep track of the length of the longest consecutive sequence found so far.

For each element *num* in the input array:

    - Check if *num - 1* is not in the set. If not, this means *num* is the start of a potential consecutive sequence.
    
    - If *num - 1* is not in the set, keep incrementing *num* by 1 and checking if *num* exists in the set. This way, you keep extending the consecutive sequence until it ends.
    c. Update the *longest_streak* to the maximum of the current *longest_streak* and the length of the current consecutive sequence.
    Return the *longest_streak*.