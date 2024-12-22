"""75. Sort Colors"""
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        #This function implements the Dutch National Flag problem using Bucket Sort 
        # to sort an array containing 
        #three distinct values: 0, 1, and 2. It first counts the occurrences of each value 
        #in a fixed-size array 
        #(bucket). Then, it overwrites the original array with 
        # the sorted values based on the counts.

        #Loom: https://www.loom.com/share/ce2e6b5bdc4942d5b97c5614732741cc
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
        for i,color in enumerate(count):
            for _ in range(color):
                nums[index] = i
                index +=1
