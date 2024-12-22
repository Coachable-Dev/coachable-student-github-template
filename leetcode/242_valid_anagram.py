"""242. Valid Anagram"""
class Solution:
    """Solution Class"""
    def isAnagram(self, s: str, t: str) -> bool:
        """
        #In this problem we are tasked to determine whether two strings are two valid anagrams.
        #Two words are valid anagrams  iff they share the same frequency of chars
        #Even if they are not in the same order.
        #Loom Explanation: https://www.loom.com/share/73fb993f5e3d4071add705f9e0ac6bdf
        """
        #First we check whether these two words have the same lenght
        if len(s) != len(t):
            return False
        #Second we create two empty hashmaps
        sCount = {}
        tCount = {}
        #We now check the frequency of each single character within both s & t
        #Time complexity: O(n)
        for char_s,char_t in zip(s,t):
            sCount[char_s] = 1 + sCount.get(char_s, 0)
            tCount[char_t] = 1 + tCount.get(char_t,0)
        #Comparing the two hashmaps for checking whether these two strings are valid anagrams
        #Time Complexity: O(n)
        for key,value in tCount.items():
            if value != sCount.get(key,-1):
                return False
        #Time complexity O(n) + O(n) = O(n)
        return True
