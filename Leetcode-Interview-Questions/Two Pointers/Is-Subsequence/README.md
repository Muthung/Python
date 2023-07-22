## Is Subsequence 

### Question 

Given two strings *s* and *t*, return *true* if *s* iss a **subsequence** of *t*, or *false* otherwise.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., *"ace"* is a subsequence of *"abcde"* while *"aec"* is not).

#### Implementation 

To determine if string *s* is a subsequence of string *t*.

Iterate through both strings simultaneously. Keeping two pointers, one for each string, and compare the characters at the corresponding positions.

If the characters match, move the pointer to the next position in their respective strings.

If they don't match, only move the pointer for *t*. At the end of *s* (i.e., the pointer for *s* reaches the end), it means all characters in *s* have beenr found in *t* in the same relative order, so *s* is a subsequence of *t*.

If the end of *t* is reached (i.e., the pointer for *t* reaches the end) before reaching the end of *s*, it means it couldn't find all characters in *s* in *t* in the same relative order, so *s* is not a subsequence of *t*.

