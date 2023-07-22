## Reverse Words in a String 

### Question 

Given an input string *s*, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in *s* will be separated by at least one space.

Return a string of the words in reverse order concactenated by a single space.

**Note** that *s* may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

#### Implementation 

Trim the leading and trailing spaces from the input string *s*.

Split the string *s* into an array of words using the space character as the delimiter.

Reverse the array of words.

Join the reversed array of words into a single string, using a single space as the seperator.

Return the reversed string.
