## Text Justification 

### Question 

Given an array of strings *words* and a width *maxWidth*, format the text such that each line has exactly *maxWidth* characters and is fully (lef and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces *' '* when necessary so that each line has exactly *maxWidth* characters.

Extra spaces betwenn words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**

> A word is defined as a character sequence consisting of non-space characters only.

> Each word's length is guaranteed to be greater than *0* and not exceed *maxWidth*.

> The input array *words* contains at least one word.

#### Implementation 

Initialize an empty array called *results* to store the formatted lines.

Initialize two variables: *line* as empty string to keep track of the current line being built, and *line_length* as 0 to keep track of the current length of the line.

Iterate through each word in the *words* array.

Check if adding the current word to the current line will exceed the *maxWidth*. If it does, it has completed building a line, Add it to the *results* array.

Determine  the number of extra spaces needed to evenly distribute between the words on the line. Calculate the total number of spaces by subtracting the total length of the words from *maxWidth*. Also, calculate the number of gaps between word on the line.

If the line conatins only one word or it's the last line, left-justify the line by appending all the words together with a single space between them, followed by the required number of extra spaces.

If the line contains more than one word and it's not the last line, distribute the extra spaces evenly between the words. Calculate the number of extra spaces to be added between each pair of words by dividing the total number of spaces by the number of gaps. Distribute any remaining spaces by adding one extra space to each gap from left to right.

Add the formatted line to the *results* array.

Continue this process until all words have been processed.

Return thhe *results* array as the final output.
