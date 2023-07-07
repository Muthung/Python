## Longest Common prefix

### Question 

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string.

#### Implementation 

The function checks the characters at each position from left to right, comparing them across all strings.

If a mismatch is found or the end of any string is reached, it returns the longest common prefix found so far.

If all characters match, it returns the complete prefix of the first string, which is guaranteed to be the longest common prefix since its the longest string in the array.
