## Merge Two Sorted Lists

### Question

You are given heads of two sorted linked lists *list1* and *list2*.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

*Return the head of the merged linked list*.

#### Implementation

Iterate through both lists simoultaneously and compare the values of the nodes.

Then, create a new merged list by selecting th esmaller value at each step.

