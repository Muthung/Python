## Valid Parantheses

### Question 

Given a string *s* containing just the characters *'(', ')', '{', '}', '[' and ']'*, determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.

    Open brackets must be closed in the correct order.

    Every close bracket has a corresponding open bracket of the same type.

#### Implementation

Use a stack data structure. 

The idea is to iterate through the characters of the input string and use a stack to keep track of the opening brackets. 

Whenever you encounter a closing bracket, you can check if it matches the corresponding opening bracket at the top of the stack. If it does, you pop the opening bracket from the stack; otherwise, the string is not valid.