"""1347. Minimun number of steps to make two strings anagram"""
class Solution:
    """Solution Class"""
    def minSteps(self, s: str, t: str) -> int:
        """
        The goal is to calculate the minimum number of steps required to make `t` an anagram of `s`.
        We will achieve this by counting the frequency of characters in both strings
        and determining the difference in character counts that need to be adjusted.
        Loom https://www.loom.com/share/
        26871858062846d8b35267e8b71c6a37?sid=428e8d4a-2828-4487-a7fb-37eb685a2813
        """
        #We will start by counting the occurences of chars for both s and t
        sCount = {}
        tCount = {}
        result = 0
        #Time Complexity: O(n)
        #We start counting for s
        for char in s:
            if char in sCount:
                sCount[char] +=1
            else:
                sCount[char] = 1
        #Time Complexity: O(n)
        #We also do the counting for t
        for char in t:
            if char in tCount:
                tCount[char] +=1
            else:
                tCount[char] = 1
        #We will calculate the difference (if there is) of sCount[char] - tCount[char]
        # and contiounsly update our result accordingly.
        #Time Complexity: O(n)
        for key,value in sCount:
            result += max(0,value - tCount.get(key,0))
        #Time Complexity O(n) + O(n) + O(n) = O(n)
        #Space Complexity O(n)
        return result
