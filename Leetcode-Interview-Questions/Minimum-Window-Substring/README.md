## Minimum Window Substring 

### Question 

Given two strings *s* and *t* of lengths *m* and *n* respectively, return the minimum window substring
of *s* such that every character in *t* (including duplicates) is included in the window.

If there is no such substring, return the empty string *""*.

The testcases will be generated such that the answer is unique.

#### Implementation 

Use the sliding window technique.

The idea is to use two pointers, *left* and *right*, to form a window and move it through the string *s*.

We expand the window to the right until it contains all the characters from *t*, and then we contract it from the left to find the minimum window that satisfies the condition.
