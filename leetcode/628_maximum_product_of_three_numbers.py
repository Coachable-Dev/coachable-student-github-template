"""628. Maximum Product of Three Numbers"""
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        """
        #Finds the maximum product of three numbers in the given list.
        #loom: https://www.loom.com/share/b7ce6f18baac4ddfa9cfae3fe37aed0c
        """
        #Time Complexity: O(n log n)
        #Space Complexity: O(1)
        #Step 1: Sort the array
        nums = sorted(nums)
        # Step 2: Consider two possible options to calculate the maximum product:
        # Option 1: Use the last three elements of the sorted array.
        # This works because if the array contains only positive numbers,
        # the three largest numbers will yield the maximum product.
        # Specifically: nums[-1] * nums[-2] * nums[-3].
        # Option 2: Use the first two elements and the last element.
        # This works if the array contains negative numbers.
        # Two negative numbers multiplied together give a positive result,
        # and multiplying them with the largest positive number (nums[-1])
        # will yield the maximum product in such cases.
        # Specifically: nums[0] * nums[1] * nums[-1].

        #Given these two possible options for both all positive/negative 
        #integers and mixed positive
        #and negative integers we will return the one which yields 
        #the largest product of three numbers.
        return max( nums[-1] * nums[-2] * nums[-3],
                    nums[0] * nums[1] * nums[len(nums)-1])

