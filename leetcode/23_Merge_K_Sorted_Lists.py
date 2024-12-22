import heapq
def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list using
    a min heap.
    Approach:
    1. Create a min heap and add the first node from each list
    2. Pop the smallest value, add it to result, and add the next
    node from that list
    3. Repeat until heap is empty
    Time: O(N log k) where N is total nodes and k is number of lists
    Space: O(k) for the heap
    :type lists: List[Optional[ListNode]]
    :rtype: Optional[ListNode]
    """
    #Handle edge cases
    if not lists:
        return None
    
    #Initialize the heap
    heap = []

    #Add first node from each list to heap
    #We need index i to break ties when values are equal
    for i, lst in enumerate(lists):
        if lst:
            #Store (value, index, node) - index breaks ties for
            #equal values
            heapq.heappush(heap, (lst.val, i, lst))
    #Create dummy head for result list
    dummy = ListNode(0)
    curr = dummy

    #Process nodes from heap
    while heap:
        val, i, node = heapq.heappop(heap)
    
        #Add node to result
        curr.next = node
        curr = curr.next

        #If this node has a next node, add it to heap
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
