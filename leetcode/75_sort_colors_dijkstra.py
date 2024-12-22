"""75. Sort Colors Dijkstra's Dutch National Flag Problem"""
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        #This function sorts an array containing three possible colors represented as 0, 1, and 2. 
        #Using Dijkstra's algorithm (Dutch National Flag Problem), the sorting is performed in-place 
        #with the help of three pointers:
        #- `l`: Tracks the boundary for 0s.
        #- `r`: Tracks the boundary for 2s.
        #- `i`: Iterates through the array.
        #The algorithm swaps elements as needed to ensure that all 0s are at the start, 
        #all 2s are at the end, and 1s are in the middle.
        #Loom: https://www.loom.com/share/ce2e6b5bdc4942d5b97c5614732741cc
        """
        #Using Dijkstra's algorithm (Dutch National Flag Problem)
        #I'll initialize both a left and right pointer
        l,r = 0, len(nums) -1
        i = 0
        #We will have to perform swapping alongisde our problem
        #So we will use an helper function to perform it
        def swap(i,j):
            # nums[i], nums[j] = nums[j], nums[i]
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        #We will now be using our pointers
        #To correctly sort our colors array
        #Time Complexity O(n)
        #Space Complexity O(1)
        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l+=1
                i+=1
            elif nums[i] == 2:
                swap(i,r)
                r -= 1
            else:
            #We will assume that the other number will be in
            #In their right position
                i+=1
