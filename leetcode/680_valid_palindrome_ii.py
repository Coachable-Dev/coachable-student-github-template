"""680. Valid Palindrome II"""
class Solution:
    """Solution Class"""
    def validPalindrome(self, s: str) -> bool:
        """
        #This problem involves checking if a string can become a palindrome
        # by removing at most one character
        #Loom https://www.loom.com/share/
        #1446e5bef8d64d87ba316bfaed8a8ec0?sid=ae466498-2798-4c37-99ea-d581a6f6b49a
        """
        #I'll start by initialazing two pointers (left,right)
        l,r = 0, len(s)-1
        #We have to iterate over a while loop until (l<r)
        #Inside our while loop we will be checking if the chars we are currently
        #pointint too are not the same.
        #If they are not the same we will be trying skipping either one from left
        #or one from right.
        #We will evaluate whether by removing one we do find a match which means
        #this will be  the char for both s[l] and s[r]
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        while l<r:
            if s[l] != s[r]:
                nextL, nextR = s[l+1:r+1], s[l:r]
                return (nextL == nextL[::-1] or nextR == nextR[::-1])
            l+=1
            r-=1
        return True
