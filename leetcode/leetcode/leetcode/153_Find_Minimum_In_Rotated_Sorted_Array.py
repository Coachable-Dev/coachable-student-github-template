def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        #If mid element is greater than high,
        #search in the right.
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            #min is in left half.
            high = mid
    return nums[low] 

    #time O(logn) for binary search
    #space O(1) no extra space
