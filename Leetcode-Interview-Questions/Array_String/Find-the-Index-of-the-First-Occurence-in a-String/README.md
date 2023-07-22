## Find the Index of the First Occurence in a string

### Question 

Given two strings *needle* and *haystack*, return the index of the first occurence of *needle* in *haystack*, or *-1* if *needle* is not part of *haystack*.

#### Implementation 

Check if the length of the needle is greater than the length of the haystack. If it is, return -1 since the needle cannot be a substring of the haystack.

Iterate through the haystack string using a loop that goes from 0 to the difference between the lengths of haystack and needle.

For each index *i* in the loop, check if a substring of the haystack starting from *i* and having the same length as the needle matches the needle string. You can use the substring function or array slicing to extract the substring.

If the substring matches the needle, return the index *i*.

If no match is found, return *-1*.
