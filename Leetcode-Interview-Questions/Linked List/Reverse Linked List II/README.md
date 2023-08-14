## Reverse Linked List II

### Question

Given the *head* of a singly linked list and two integers *left* and *right* where *left <= right*, reverse the nodes of the list from position *left* to position *right*, and return the reversed list.

#### Implementation

Create a mapping of original nodes to their corresponding copied nodes.

Traverse the original linked list, create new nodes for the copied linked list, and populate the mapping.

Traverse the original linked list again, and update the next and random pointers for the copied nodes using the mapping.