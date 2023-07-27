## Valid Anagram

### Question 

Given two strings *s* and *t*, return *true* if *t* is an anagram of *s*, and *false* otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#### Implementation 

Ensure that they have the same characters with the same frequency, even if the characters are in different orders.

Ensure the function checks if the lengths of the two strings are equal; if not, it directly return 
*False*, as anagrams must have the same length.

Then, it creates dictionaries to store the frequency of characters in each string.

After counting the frequencies of characters in both strings, it compares the two dictionaries.

If they are the same, the function returns *True*, indicating that *t* is an anagram of *s*. Otherwise, it returns *False*.