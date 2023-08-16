## Remove Nth Node from End of List

### Question

Given the *head* of a linked list, remove the *nth* node from the end of the list and return its head.

#### Implementation

Use a two-pointer approach.

Create two pointers, first and second, and initialize them to point to the head of the linked list.

Move the first pointer n nodes ahead. This ensures that the distance between first and second is n nodes.

Move both first and second pointers simultaneously until first reaches the end of the linked list (i.e., first reaches the last node).

At this point, the second pointer will be pointing to the (n+1)th node from the end. Update the next pointer of the node pointed to by the second pointer to skip the nth node.

Return the head of the modified linked list.