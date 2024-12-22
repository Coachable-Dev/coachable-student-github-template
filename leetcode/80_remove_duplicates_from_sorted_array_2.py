"""80. Remove Duplicates from sorted array II"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        #Removes duplicates from the sorted array `nums`,
        #allowing at most two occurrences of any element.
        #Loom: https://www.loom.com/share/16734f04846f4f3bbdfb590576c50b1d
        """
        #I aim to solve this problem with a Time Complexity O(n)
        #Space complexity I aim as the problem constraints suggests to be within O(1)
        #To solve this problem we will be first declaring our two pointers
        #i,k respectively starting at position: 2
        i, k = 2,2
        #We will implement an iterative while loop that will function
        #until k< len(nums)
        while k<len(nums):
            #We will be checking for further duplicates (that exceeds more than 2)
            #And we will remove it by sliding back the array numbers
            if nums[k] != nums[i-2]:
                nums[i] = nums[k]
                i+=1
            k+=1
        return i
