from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """_summary_

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """

        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                length = 1
                next_num = num + 1

                while next_num in num_set:
                    length += 1
                    next_num += 1
                longest = max(length, longest)

        return longest
