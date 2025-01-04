from typing import List
from itertools import permutations

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return list(map(list, permutations(nums)))
#time O(n!)
#space O(n*n!)
