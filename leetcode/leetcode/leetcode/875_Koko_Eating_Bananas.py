def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    [1,2,3,4,5,6,7,8,9,10,11] 
    """
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2

        #Calculate hours needed to eat all piles
        #at current speed.
        hours_spent = sum((pile - 1) // mid + 1 for pile in piles)

        #if hours spent is more than allowed,
        #increase speed.
        if hours_spent > h:
            left = mid + 1
        #If hours spent is within the limit,
        #try to minimize speed.
        else:
            right = mid
    return left

    #time O(n log m) n is number of piles,
    #m is max pile size.
    #space O(1) no extra space used
