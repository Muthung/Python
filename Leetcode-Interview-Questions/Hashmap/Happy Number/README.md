## Happy Number

### Question

Write an algorithm to determine if a number n is happy.

A **happy** number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.

    Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.

    Those numbers for which this process ends in 1 are happy.

Return *true* if *n* is a happy number, and *false* if not.

#### Implementation 

Need to repeatedly replace the number by the sum of the squares of its digits until we either reach 1 (happy number) or fall into a cycle.

To detect cycles, use a set to store the numbers we have seen so far. If it encounter a number that is already in the set, it means it's in a cycle and the number is not happy.

This algorithm will repeatedly calculate the sum of the squares of digits of the input number *n* until it either reach 1 or encounter a number that it has seen before, indicating a cycle.

If it reaches 1, the function returns *True*, indicating that the number is happy; otherwise, it returns *False*.