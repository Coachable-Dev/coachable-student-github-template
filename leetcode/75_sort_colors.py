#Loom: https://www.loom.com/share/ce2e6b5bdc4942d5b97c5614732741cc
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        #Given our small sample of possible colors we will solve this problem
        #by using Bucket Sort.

        #We first declare our bucket array for our 3 possible colors.
        # Since we only have 3 possible colors (0, 1, 2), we create an array of size 3.
        count = [0,0,0]
        #Step 2: We now fill the buckets with their respective colors
        # We iterate through the nums array to count the colors 
        for color in nums:  
            count[color] +=1

        # We will now iterate through the `count` array to overwrite nums.
        # Start from index 0 and place the correct number of each color in order.
        index = 0
        for i in range(len(count)):
            for _ in range(count[i]):
                nums[index] = i
                index +=1