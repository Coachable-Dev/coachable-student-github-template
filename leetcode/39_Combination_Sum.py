def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    We use backtracking to try different combinations of numbers.
    Backtracking allows us to explore all possibilites efficiently.
    """
    def backtrack(remain, curr, start):
        #Base case: If remaining sum is 0, we found 
        #a valid combination
        if remain == 0:
            result.append(curr[:])
            return
        
        for i in range(start, len(candidates)):
            #Skip if the current number is too large
            if candidates[i] > remain:
                continue
            
            #Include the current number in combination
            curr.append(candidates[i])
            #Recursive call with remaining sum
            #We pass i instead of i + 1 because 
            #we can reuse same number
            backtrack(remain - candidates[i], curr, i)
            #Backtrack by removing the number
            curr.pop()
        
    #Sort candidates to optimize and handle cases where
    #the number > target
    candidates.sort()
    result = []
    backtrack(target, [], 0)
    return result

    #time O(N^T/M) N is the number of candidates. T is the
    #target, and M is the min values among candidates.
    #space O(T/M) for the recursion stack depth.
