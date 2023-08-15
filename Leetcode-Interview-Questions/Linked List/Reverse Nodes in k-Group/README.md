## Reverse Nodes in k Group

### Question

Given the *head* of alinked list, reverse the nodes of the list *k* at a time, and return the *modified list*.

*k* is a positive integer and is less than or eqqual to the length of the linked list. If the number of nodes is not a mutliple of *k* then left out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only node themselves may be changed.

#### Implementation

The function **reverseKGroup** takes the head of a linked list and an integer *k* as inputs and returns the modified list where nodes are reversed in groupd of *k*.

It defines two helper functions **reverseLinkedList** to reverse a linked list and **getLength** to calculate the length of the list.

The main function iterates through the linked list in groups of *k*, reverse each group using the **reverseLinkedList** function, and updates the pointers accordingly.

