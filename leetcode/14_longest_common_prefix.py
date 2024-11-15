"""14. Longest Common Prefix"""

from typing import List

class Solution:
    """Solution Class for finding the longest common prefix."""
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix in a list of strings.

        Process:
        - Start with the first string as the initial prefix.
        - Iteratively compare the prefix with each subsequent string.
        - Shrink the prefix from the end until it matches the start of the current string.
        - If the prefix becomes empty, return an empty string.

        Edge Cases:
        - If the input list is empty, return an empty string.
        - If the list contains only one string, return that string as the prefix.

        Args:
            strs (List[str]): List of input strings.
        
        Returns:
            str: The longest common prefix, or an empty string if none exists.
        """
        
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
