"""13. Roman to Integer"""
class Solution:
    """Solution Class"""
    def romanToInt(self, s: str) -> int:
        """
        #In this problem, we are tasked with converting a Roman numeral into an integer.
        #We will take advantage of a dictionary to map each Roman numeral to its integer equivalent
        # and perform the appropriate operations accordingly
        # When calculating Roman numerals, it is pivotal to understand
        # that if a smaller value is placed before a larger one,
        # it means it needs to be subtracted from the larger one.
        # We will use our indices iand  i + 1 i+1 to handle this accordingly.
        # Loom Explanation: https://www.loom.com/share/
        # 547413d81386454a8efd022aed8aff1e?sid=e5e45965-4bd0-488b-ab45-019f8be9a695
        """
        #First we initialize our dictionary by mapping each roman numerals to integers
        hashmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        #Declaring our total
        total = 0
        n = len(s)
        i = 0
        #Iterating with a while loop over the 's' and checked by using our hashmaps
        #the respective roman numerals integer values and proceeded with either adding
        # or subtracting accordingly.
        #We also moved by index +2 in case we performed a subtraction
        #We instead moved our index by 1 in case we just performed an addition
        #O(n)
        while i<n:
            if i + 1 < n and hashmap[s[i]] < hashmap[s[i+1]]:
                total += hashmap[s[i+1]] - hashmap[s[i]]
                i +=2
            else:
                total += hashmap[s[i]]
                i+=1
        #Finally the total gets returned
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        return total
