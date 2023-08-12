def mergeTwoLists(list1, list2):
    dummy_head = ListNode()  # Create a dummy head node for the merged list
    current = dummy_head  # Initialize a pointer to the current node of the merged list

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach any remaining nodes from list1 or list2
    current.next = list1 if list1 else list2

    return dummy_head.next