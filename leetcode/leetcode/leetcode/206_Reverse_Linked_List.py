def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    Iterative approach
    """
    #Initialize previous and current pointers
    prev = None
    current = head

    #Traverse the list.
    while current:
        #Store the next node before changing
        #the links
        next_node = current.next
        #Reverse the link
        current.next = prev
        #Move pointers one step forward.
        prev = current
        current = next_node

    #Return the new head(last node of original list)
    return prev

    #time O(n) iterate entire array once.
    #space O(1) no extra space used/needed.
