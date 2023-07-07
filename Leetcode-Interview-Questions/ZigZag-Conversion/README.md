## ZigZag Conversion

### Question 

The string *PAYPALISHIRING* is written in a zigzag pattern on a given number of rows like this: (you want to display this pattern in a fixed font for better legibility)

    P A H N
    APLSIIG
    Y I R
    
And then read line by line: *PAHNAPLSIIGYIR*

Write the code that wil take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);
    
#### Implementation 

The function works by maintaining a list of strings, *rows*, where each element represents a row in the zigzag pattern. 

It iterates over each character in the input string and appends the character to the appropriate row.

The *index* variable keeps track of the current row, and the *step* variable determines whether we move up or down the rows.

When *index* reaches either the first or last row, the *step* is reversed to change the direction. The function joins all thee rows and returns the converted string.
