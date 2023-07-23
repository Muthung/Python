## Isomorphic Strings

### Question 

Given two strings *s* and *t*, determine if they are isomorphic.

Two strings *s* and *t* are isomorphic if the characters in *s* can be replaced to get *t*.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

#### Implementation 

Use two dictionaries to keep track of the mappings from *s* to *t* and from *t* to *s*.

If at any point, find a conflicting mapping, return False immediately.

Otherwise, if it completes the traversal without any conflicts, return True, indicating that the strings are isomorphic.