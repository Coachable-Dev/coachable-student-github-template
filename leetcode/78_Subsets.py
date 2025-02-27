def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    We use backtracking to generate all possible subsets.
    For each element, we have two choices:
    Include it in the current subset
    Exclude it from the current subset
    """
    result = []

    def backtrack(start, current):
        #Add the current subset to our result
        result.append(current[:])

        #Try adding each remaining subset to our current subset
        for i in range(start, len(nums)):
            #Include nums[i] to our current subset
            current.append(nums[i])
            #Recursively generate subsets with nums[i] included
            backtrack(i + 1, current)
            #Backtrack by removing nums[i] to try next number
            current.pop()
        
    backtrack(0, [])
    return result

#time O(2^n) for each element, we can make at most 2 choices, so its 2 to the power of the length of n.
#soace O(n) the recursion stack is the size of n. 
