"""55. Jump Game"""
class Solution:
    """Solution Class"""
    def canJump(self, nums: list[int]) -> bool:
        """
        #This function determines if it is possible to jump from the first index of the array 
        #to the last index. The solution uses a greedy approach by working backward from the 
        #last index and checking if the current index can "jump" to or beyond the target index.
        #Loom: https://www.loom.com/share/3ad998725e1c474cb0f5f0be9323139f
        """
        #Time Complexity: O(n)
        #Space Complexity: O(1)

        #We use only a single variable `target` for tracking.
        #We nitialize the target as the last index of the array.
        #This represents the position we need to reach (or surpass).
        target = len(nums) -1

        # We will be iterating with a for loop in range of len(nums) and
        # we will be moving backward and check whether depending how many steps
        # behind we can go if we can reach our final target which happens the first element
        # of our array nums[0]

        for i in range(len(nums)-1, -1,-1):
            if nums[i] + i >= target:
                # Update the target to the current index `i`
                # because it's now the furthest we need to reach.
                target = i

        return True if target == 0 else False
