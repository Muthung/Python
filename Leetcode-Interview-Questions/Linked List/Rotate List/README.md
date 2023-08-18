## Rotate List

### Question

Given the *head* of a linked list, rotate the list to the right by *k* places.

#### Implementation

**ListNode Class:** 

First, a ListNode class is defined to represent nodes in the linked list. Each node has two attributes: *val* to store the value of the node, and *next* to store the reference to the next node in the list.

**rotate_right Function:**

The *rotate_right* function takes two parameters: *head,* which is the head of the linked list, and *k*, the number of places to rotate the list to the right.
        
The function first handles two base cases: if the *head* is *None* (empty list) or if *k* is *0*, it returns the original *head* as no rotation is needed.

**Calculate Length:**

The length of the linked list is calculated by traversing the list from the *head* node to the last node. The *length* variable is incremented for each node encountered.

**Adjust k:**

The value of *k* is adjusted by taking its modulus with the length of the list. This is done to handle cases where *k* is larger than the length of the list, as rotating by a full cycle is equivalent to no rotation.

**Find New Head and Tail:**

To rotate the list, we need to find the new head and tail of the rotated list. The *current* variable is used to traverse the list from the head node.

We traverse the list until *length - k - 1* nodes to find the node that will be the new tail of the rotated list.
        
The *new_head* is set as the next node of the *current* node, and the *next* reference of the *current* node is set to *None* to disconnect the rotated portion of the list.

**Update Tail and Connect Lists:**

The original tail of the list is found by traversing from the *new_head* to the end of the list. The *tail* is updated to point to the original *head*.
        
The *next* reference of the original tail is set to the *head* of the list, effectively connecting the end of the original list to the beginning.

**Return New Head:**
        
The function returns the *new_head*, which is the new starting point of the rotated list.