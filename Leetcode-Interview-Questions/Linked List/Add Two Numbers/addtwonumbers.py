def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        sum = carry

        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next

    return dummy_head.next