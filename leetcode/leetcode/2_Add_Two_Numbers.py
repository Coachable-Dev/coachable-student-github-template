def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    #Create dummy head for list construction
    dummy = ListNode()
    current = dummy

    #Carry to handle digit overflow
    carry = 0

    #Iterate while either list has nodes or
    #there's a carry
    while l1 or l2 or carry:
        #Get values defaulting to 0 if list exhausted.
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        #Calculate total sum for current digit
        total = val1 + val2 + carry

        #Update carry and current digit
        carry = total // 10
        current.next = ListNode(total % 10)

        #Move pointers forward
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    #Return the next node of dummy
    return dummy.next

    #time O(n)
    #space O(1)
