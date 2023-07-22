## Longest Substring Without Repeating Characters

### Question 

Given a string *s*, find the length of the longest substring without repeating characters.

#### Implementation 

Use a sliding window approach.

Initialize two pointers, *start* and *end*, both pointing to the start of the string *s*.

Initialize a variable *max_length* to store the maximum length of the substring without repeating characters. Also, initialize an empty set *seen* to keep track of the characters in the current substring.
    
Iterate through the string *s* using the *end* pointer until it reaches the end of the string:

        Check if the character at the *end* pointer is already in the *seen* set.
            
        If it is not in the set, add the character to the *seen* set and move the *end* pointer one 
        step forward.
        
        If it is in the set, update the *max_length* with the maximum value between *max_length* and 
        the size of the *seen* set, then move the *start* pointer one step forward and remove the
        character at the *start* pointer from the *seen* set. 
        
        Repeat this step until the character at the *end* pointer is not in the seen set.
        
After the loop, update the *max_length* with the maximum value between *max_length* and the size of the *seen* set again to handle cases where the longest substring ends at the last character of *s*.
    
Return the *max_length*.
