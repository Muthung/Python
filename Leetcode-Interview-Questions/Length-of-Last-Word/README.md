## Length of Last Word

### Question 

Given a string *s* consisting of words and spaces, return the length of the last word in the string.

A **word** is a maximal *substring* consisting of non-space characters only.

#### Implementation 

Trim the input string *s* to remove leading and trailing spaces.

Find the index of the last space in the trimmed string.

Extract the substring starting from the index of the last sapce + 1 to the end of the string.

Return the length of the extracted substring.
