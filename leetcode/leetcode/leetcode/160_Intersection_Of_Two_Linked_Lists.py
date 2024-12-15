def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    Approach 1: Hash Set. Store all nodes of
    List A in a set. Traverse List B and see if
    any nodes of A in B. Uses O(m + n) time, 
    but O(m) space for the set.
    Approach 2: Two Pointer. Use two pointers to
    traverse both lists. When a pointer reaches
    the end, redirect to the other list's head.
    Both pointers travel same total distance.
    Handles different list lengths. Gives us
    O(1) space, more optimal.
    """
    #If either list empty, no intersection.
    if not headA or not headB:
        return None
    
    #pointers for both lists.
    pA, pB = headA, headB

    #Traverse both lists
    while pA != pB:
        #Move pointers, when reaching end,
        #redirect to other list's head.
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next

    #Return intersection point or None.
    return pA

    #time O(m + n) for traversing two lists.
    #space O(1) no extra space used.
