## Add Two Numbers

### Question

You are given two **non-empty** linked list representing two non-negative integers. The digits are stored in **reserve-order**, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two Numbers do not contain any leading zero, except the number 0 itself.

#### Implementation

Simulate the process by adding two numbers digit by digit while maintaining a carry.

Traverse both linked list simultaneously, adding corresponding digits along with the carry, and updating the carry.

If one of the linked list becomes empty, treat the remaining digits as zeros. Finaaly, create a new linked list to store the result.