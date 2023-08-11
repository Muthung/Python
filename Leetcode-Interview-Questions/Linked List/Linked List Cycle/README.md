## Linked List Cycle

### Question

Given *head*, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is soome node in the list that can be reached again by contiously following the *next* pointer. Internally, *pos* is used to denote the index of the node that tail's *next* pointer is connected to.

**Note that *pos* is not passed as a parameter.**

Return *true* if there is a cycle in the linked list. Otherwise, return *false.*

#### Implementation

Use **Floyd's Cycle Detection Algorithm ( Tortoise and Hare Algorithm )**.

This algorithm uses two pointers, one slow and one fast, to traverse the linked list.
If there is a cycle in the linked list, the fast pointer will eventually catch up to the slow pointer.
