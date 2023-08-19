## Partition List

### Question

Given the *head* of a linked list and a value *x*, partition it such that all nodes **less then x** comebefore nodes **greater thhan or equal to x**.

You should preserve the original relative order of the nodes in each of the two partitions.

#### Implementation

The function takes the *head* of the linked list and the value *x* as input.

Two dummy nodes (*bf_head* and *af_head*) are created to serve as the starting points for the two partitions: nodes less than *x* and nodes greater than or equal to *x*.

The before and after pointers are used to keep track of the last node in each partition.

A *current* pointer is used to traverse the original linked list.

During traversal, nodes less than *x* are appended to the *bf* partition and nodes greater than or equal to *x* are appended to the *af* partition.

After traversing the entire list, the last node's *next* pointers in both partitions are set to *None* to terminate the partitions.

The *bf* partition's *next* is then connected to the *af_head.next*, effectively merging the two partitions.

The function returns *bf_head.next*, which is the head of the linked list after partitioning.

