## Remove Duplicates from Sorted List II

### Question

Given the *head* of a sorted linked list, delete all node that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list **sorted** as well.

#### Implementation

The *deleteDuplicates* function takes the head of a sorted linked list as input and returns the head of the modified linked list.

Inside the *deleteDuplicates* function:

First it handle the cases where the linked list is empty or has only one node. In those cases, there are no duplicates to remove, so it simply return the head.

Creates a *dummy* node at the beginning of the linked list. This dummy node serves as a placeholder and makes it easier to handle cases where the head needs to be removed.

Initialize a *prev* pointer to point to the *dummy* node. This pointer will help us keep track of the previous node while traversing the linked list.

Enters a loop that traverses the linked list. For each node *head*:

Checks if *head* has a next node and if the value of *head* is the same as the value of the next node. If they are the same, it means we have duplicates.

Enters an inner loop to skip all the duplicate nodes, updating the *head* pointer until we reach a node with a different value.

Once it has skipped all duplicates, it updates the *next* pointer of the previous node *(prev.next)* to point to the node after the last duplicate node (i.e., *head.next*).

If there are no duplicates, it simply update the *prev* pointer to the current *head* node.

Finally, it updates the *head* pointer to the next node and repeat the process until we have traversed the entire linked list.

After the loop, it returns the *next* node of the *dummy* node, which is the new head of the modified linked list containing only distinct values.

