## Basic Calculator

### Question

Given a string *s* representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as *eval()*.

#### Implementation

Iterate through the given expression character by character and processes operands, signs, parantheses, and operators.

It uses a stack to keep track of previous results and signs when encountering parantheses.

The final result is calculated summing up the individual componenets.