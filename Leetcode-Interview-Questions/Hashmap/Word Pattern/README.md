## Word Pattern

### Question 

Given a *pattern* and a string *s*, find if *s* follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in *pattern* and a **non-empty** word in *s*.

#### Implementation 

Split the string *s* into individual words.

Create two dictionaries: one to map characters from the pattern to words, and the other to map words back to characters from the pattern.

Traverse through both the pattern and the list of words simultaneously.

Check if each character in the pattern is already present in the pattern-to-word dictionary, and if the corresponding word is the same as the current word in the list. If not, return *False*.

Also, check if the current word in the list is already present in the word-to-pattern dictionary, and if the corresponding character in the pattern is the same as the current character. If not, return *False*.

If both conditions pass, continue to the next character-word pair.

If the loop completes successfully, return *True*.