"""67. Add Binary"""
class Solution:
    """Solution Class"""
    def addBinary(self, a: str, b: str) -> str:
        """
        #This problem gives us two binary numbers in strings format
        # and our aim is to add them together.
        # We will take advantage of ord() to calcualte the int value of our chars
        # By doing so we can then add together the values, calculate the respective carry
        # and add it it before while we update our final solution.
        # Loom: https://www.loom.com/share/
        # be44b18673cb412ab685ce4c9503be6a?sid=b0aff3ea-8e21-4013-83b3-af619d7fa4c8
        """
        #First initalizing my solution string
        sol = ""
        #Reverting the strings to ensure proper addition
        #Time Complexity: O(n)
        a,b = a[::-1], b[::-1]
        #Initializing my carry to 0
        carry = 0
        #Time Complexity O(n)
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            total = digitA + digitB + carry
            char = str(total %2)
            #O(1)
            sol = char + sol
            carry = total // 2
            #O(n)
        if carry:
            sol = str(carry) + sol
            #Time Complexity O(n)
            #Space Complexity O(n)
        return sol
