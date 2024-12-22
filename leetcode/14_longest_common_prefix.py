"""14. Longest Common Prefix"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        # We are tasked with finding the Longest Common Prefix using an iterative nested for loop.
        # We start by initializing an empty string `result` to store our output.
        # The outer for loop iterates over the range of the first string in the given strings array.
        # To check for common characters across all strings in `strs`, we use an inner for loop.
        # In the inner loop, we check the following conditions:
        # 1) If `i` equals the length of the string:
        #    - This means we have reached the end of the string,
        # so there are no more characters to check.
        #      In this case, we return `result` as it is because the word has terminated.
        # 2) If `string[i] != strs[0][i]`:
        #    - This means the character at index `i` in the current string does not match
        #      the character at the same index in `strs[0]`, which we are using for comparison.
        #      If this happens, we return `result`.
        # As long as neither condition is met, we are finding matching characters. These common
        # characters constitute the common prefix, so we append them to `result`.
        # Eventually, once the conditions are triggered or the loop completes, 
        # we return `result`.
        # Time Complexity: O(n * m), where `n` is the number of strings,
        # and `m` is the length of the first string.
        # Space Complexity: O(1), as no extra space is used.ch will constitute to common prefixes
        #Either by the above conditon getting activated or not we will return result. 
        #Loom Explanation  https://www.loom.com/share/fd45b55f6d75421f84a633995ba9cfc5
        """
        #Initializing an empty string for storing our result
        result = ""
        #We will be using an interative for loop to compare
        #the first string to the other strings's characters.
        #Reason for so is to see whether we can find any consequtives/indivudal matches
        #O(n)
        for i in range(len(strs[0])):
            #O(m)
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        #Time complexity O(n) * O(m) = O(n*m)
        #Space Complexity: O(1)
        return result
