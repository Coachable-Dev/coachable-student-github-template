#Loom: https://www.loom.com/share/3ad998725e1c474cb0f5f0be9323139f

class Solution:
    def canJump(self, nums: list[int]) -> bool:
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